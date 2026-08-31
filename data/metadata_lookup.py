"""
ASCENT — Metadata secondary-data lookup
=========================================

Mirrors the workbook's 55,116-row `Metadata` sheet. When the user turns on
"Use secondary data?" and selects a location, this module returns the
pre-populated values for that district (and its state), mapped to the
questionnaire's form-field names.

Data lives in data/metadata.db (SQLite, indexed by state+district). We keep it
in SQLite rather than an in-memory dict so the 13.5 MB dataset doesn't bloat
process memory or slow startup — each lookup is a single indexed query.
"""
import os
import sqlite3

_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metadata.db")


def _conn():
    # check_same_thread=False so the gunicorn threads can share the connection
    c = sqlite3.connect(_DB_PATH, check_same_thread=False)
    c.row_factory = sqlite3.Row
    return c


# ─── Mapping: (sector, question) — with optional subsector/fuel — → form field ──
# Each metadata row is matched to at most one questionnaire input. The key is a
# tuple of lowercased (sector, question) and we disambiguate on fuel where a
# question repeats across fuels (e.g. transport vehicle by Petrol/Diesel).
#
# Value is the form-field `name` attribute the number should populate.

# Basic Info
_BASIC = {
    "population": "population",
    "annual population growth rate % (average last 10 years)": "pop_growth_rate",
    "annual population growth rate": "pop_growth_rate",
    "gdp (crore ₹)": "gdp",
}

# Transport — VKT method vehicle counts. Metadata splits by fuel; the web form's
# VKT block is fuel-agnostic per vehicle class, so we sum fuels per vehicle.
_TRANSPORT_VEHICLE_FIELD = {
    "passenger automobiles (cars and auto)": "vkt_car_count",
    "motorcycle":                            "vkt_motorcycle_count",
    "taxi":                                  "vkt_taxi_count",
    "heavy-duty truck":                      "vkt_hdtruck_count",
    "bus - standard":                        "vkt_bus_count",
}

# Solid waste
_SOLID_WASTE = {
    "solid waste generation (tpd)": "sw_generation_tpd",
}

# AFOLU livestock
_LIVESTOCK = {
    "dairy cow":  "dairy_cow_crossbred",
    "buffalo":    "dairy_buffalo",
    "sheep":      "sheep",
    "goat":       "goat",
    "goats":      "goat",
    "swine":      "swine",
    "poultry":    "poultry",
    "horses":     "live_horse",
    "camels":     "live_camel",
}

# IPPU production
_IPPU = {
    "production": {          # disambiguated by subsector
        "cement":    "cement_clinker",
        "steel":     "ippu_iron_steel_total",
    },
}


def _map_record(rec) -> tuple | None:
    """Return (field_name, value, meta) if this record maps to a form field."""
    sector = (rec["sector"] or "").strip().lower()
    question = (rec["question"] or "").strip().lower()
    subsector = (rec["subsector"] or "").strip().lower()
    value = rec["value"]
    meta = {
        "unit": rec["unit"], "source": rec["source"], "year": rec["year"],
        "sector": rec["sector"], "question": rec["question"],
    }

    if sector == "basic info" and question in _BASIC:
        return (_BASIC[question], value, meta)

    if sector == "transportation" and question in _TRANSPORT_VEHICLE_FIELD:
        # Sum across fuels handled by caller (accumulate)
        return (_TRANSPORT_VEHICLE_FIELD[question], value, {**meta, "_accumulate": True})

    if sector == "solid waste" and question in _SOLID_WASTE:
        return (_SOLID_WASTE[question], value, meta)

    if sector == "afolu" and question in _LIVESTOCK:
        return (_LIVESTOCK[question], value, {**meta, "_accumulate": True})

    if sector == "ippu" and question == "production":
        field = _IPPU["production"].get(subsector)
        if field:
            return (field, value, meta)

    return None


def lookup(state: str, district: str) -> dict:
    """Return {field_name: {value, unit, source, year, sector, question}} for a
    district. District-tier rows are preferred; state-tier rows fill Basic-Info
    fields (GDP, growth) that are only published at state level.
    """
    if not state:
        return {}
    filled = {}
    accumulators = {}   # field -> running total (for fuel-split transport, livestock)

    with _conn() as conn:
        # District-tier rows
        if district:
            rows = conn.execute(
                "SELECT * FROM metadata WHERE tier='District' AND state=? AND district=?",
                (state, district),
            ).fetchall()
        else:
            rows = []
        # State-tier rows (Basic Info like GDP that isn't at district level)
        state_rows = conn.execute(
            "SELECT * FROM metadata WHERE tier='State' AND state=?",
            (state,),
        ).fetchall()

    def _apply(rows):
        for rec in rows:
            mapped = _map_record(rec)
            if not mapped:
                continue
            field, value, meta = mapped
            if meta.get("_accumulate"):
                accumulators[field] = accumulators.get(field, 0) + (value or 0)
                # keep the meta (source/unit) from the first contributing row
                if field not in filled:
                    filled[field] = {"value": accumulators[field], **_clean_meta(meta)}
                else:
                    filled[field]["value"] = accumulators[field]
            else:
                # Non-accumulating: district row wins; don't overwrite if present
                if field not in filled:
                    filled[field] = {"value": value, **_clean_meta(meta)}

    _apply(rows)
    # State rows only fill fields not already set by district data
    _apply(state_rows)

    return filled


def _clean_meta(meta: dict) -> dict:
    return {
        "unit":     meta.get("unit"),
        "source":   meta.get("source"),
        "year":     meta.get("year"),
        "sector":   meta.get("sector"),
        "question": meta.get("question"),
    }


def available() -> bool:
    """True if the metadata DB is present."""
    return os.path.exists(_DB_PATH)

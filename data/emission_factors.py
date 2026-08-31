"""
Sectoral Emission Factors — extracted directly from the "Emission Factor" sheet
of WRI_India___ASCENT_Beta_V9.xlsm. Do not edit by hand; re-run the extractor.

All fuel EFs are in t/TJ; electricity in t/MWh.
CH4 and N2O are stored in raw IPCC units — multiply by the appropriate GWP
(from data.gwp) at the use site.
"""

# ─── Per-sector EF tables ─────────────────────────────────────────────────
# Structure: EF_BY_SECTOR[sector_name][activity_name] = {co2, ch4, n2o, unit}
EF_BY_SECTOR = {
    'Residential': {
        'Electricity': {'co2': 0.823, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/MWh'},
        'LPG': {'co2': 63.1, 'ch4': 0.005, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Firewood': {'co2': 112.0, 'ch4': 0.3, 'n2o': 0.004, 'unit': 't/TJ'},
        'Coal (charcoal)': {'co2': 112.0, 'ch4': 0.2, 'n2o': 0.001, 'unit': 't/TJ'},
        'PNG/City Gas': {'co2': 56.1, 'ch4': 0.005, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Kerosene': {'co2': 71.9, 'ch4': 0.01, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Diesel Gen set': {'co2': 74.1, 'ch4': 0.01, 'n2o': 0.0006, 'unit': 't/TJ'},
    },
    'Commercial': {
        'Electricity': {'co2': 0.823, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/MWh'},
        'LPG': {'co2': 63.1, 'ch4': 0.005, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Firewood': {'co2': 112.0, 'ch4': 0.3, 'n2o': 0.004, 'unit': 't/TJ'},
        'Coal (charcoal)': {'co2': 112.0, 'ch4': 0.2, 'n2o': 0.001, 'unit': 't/TJ'},
        'PNG/City Gas': {'co2': 56.1, 'ch4': 0.05, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Kerosene': {'co2': 71.9, 'ch4': 0.01, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Diesel Gen set': {'co2': 74.1, 'ch4': 0.01, 'n2o': 0.0006, 'unit': 't/TJ'},
    },
    'Institutional': {
        'Electricity': {'co2': 0.823, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/MWh'},
        'LPG': {'co2': 63.1, 'ch4': 0.005, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Firewood': {'co2': 112.0, 'ch4': 0.3, 'n2o': 0.004, 'unit': 't/TJ'},
        'Coal (charcoal)': {'co2': 112.0, 'ch4': 0.2, 'n2o': 0.001, 'unit': 't/TJ'},
        'PNG/City Gas': {'co2': 56.1, 'ch4': 0.05, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Kerosene': {'co2': 71.9, 'ch4': 0.01, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Diesel Gen set': {'co2': 74.1, 'ch4': 0.01, 'n2o': 0.0006, 'unit': 't/TJ'},
    },
    'Manufacturing': {
        'LPG': {'co2': 63.1, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Biodiesels': {'co2': 70.8, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Biogasoline': {'co2': 70.8, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Bitumen': {'co2': 80.7, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Coal (charcoal)': {'co2': 112.0, 'ch4': 0.2, 'n2o': 0.004, 'unit': 't/TJ'},
        'Coal (other bituminous)': {'co2': 94.6, 'ch4': 0.01, 'n2o': 0.0015, 'unit': 't/TJ'},
        'Coal (Sub - Bituminous)': {'co2': 96.1, 'ch4': 0.01, 'n2o': 0.0015, 'unit': 't/TJ'},
        'Coal (Lignite)': {'co2': 101.0, 'ch4': 0.01, 'n2o': 0.0015, 'unit': 't/TJ'},
        'Coke': {'co2': 107.0, 'ch4': 0.01, 'n2o': 0.0015, 'unit': 't/TJ'},
        'Coking coal': {'co2': 94.6, 'ch4': 0.01, 'n2o': 0.0015, 'unit': 't/TJ'},
        'Anthracite': {'co2': 98.3, 'ch4': 0.01, 'n2o': 0.0015, 'unit': 't/TJ'},
        'Compressed Natural Gas (CNG)': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Diesel oil': {'co2': 74.1, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Ethanol': {'co2': 61.6, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Gas oil': {'co2': 74.1, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Paraffin': {'co2': 73.3, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Liquefied Natural Gas (LNG)': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Lubricants': {'co2': 73.3, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Municipal wastes (non-biomass fraction)': {'co2': 91.7, 'ch4': 0.03, 'n2o': 0.004, 'unit': 't/TJ'},
        'Municipal wastes (biomass fraction)': {'co2': 100.0, 'ch4': 0.03, 'n2o': 0.004, 'unit': 't/TJ'},
        'Naphtha': {'co2': 73.3, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Natural gas': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Other biogas': {'co2': 54.6, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Other Liquid BioFuels': {'co2': 79.6, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Petroleum coke': {'co2': 97.5, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Residual fuel oil': {'co2': 77.4, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Sludge gas': {'co2': 54.6, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Town gas or city gas': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0001, 'unit': 't/TJ'},
        'Wood or wood waste': {'co2': 112.0, 'ch4': 0.03, 'n2o': 0.004, 'unit': 't/TJ'},
        'Electricity': {'co2': 0.823, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/MWh'},
        'Hydrogen': {'co2': 0.0, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/TJ'},
    },
    'Energy Industries': {
        'LPG': {'co2': 63.1, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Biodiesels': {'co2': 70.8, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Biogasoline': {'co2': 70.8, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Bitumen': {'co2': 80.7, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Coal (charcoal)': {'co2': 112.0, 'ch4': 0.2, 'n2o': 1.092, 'unit': 't/TJ'},
        'Coal (other bituminous)': {'co2': 94.6, 'ch4': 0.01, 'n2o': 0.40950000000000003, 'unit': 't/TJ'},
        'Coal (Sub - Bituminous)': {'co2': 96.1, 'ch4': 0.01, 'n2o': 0.40950000000000003, 'unit': 't/TJ'},
        'Coal (Lignite)': {'co2': 101.0, 'ch4': 0.01, 'n2o': 0.40950000000000003, 'unit': 't/TJ'},
        'Coke': {'co2': 107.0, 'ch4': 0.01, 'n2o': 0.40950000000000003, 'unit': 't/TJ'},
        'Coking coal': {'co2': 94.6, 'ch4': 0.01, 'n2o': 0.40950000000000003, 'unit': 't/TJ'},
        'Anthracite': {'co2': 98.3, 'ch4': 0.01, 'n2o': 0.40950000000000003, 'unit': 't/TJ'},
        'Compressed Natural Gas (CNG)': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Diesel oil': {'co2': 74.1, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Ethanol': {'co2': 61.6, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Gas oil': {'co2': 74.1, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Paraffin': {'co2': 73.3, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Liquefied Natural Gas (LNG)': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Lubricants': {'co2': 73.3, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Municipal wastes (non-biomass fraction)': {'co2': 91.7, 'ch4': 0.03, 'n2o': 1.092, 'unit': 't/TJ'},
        'Municipal wastes (biomass fraction)': {'co2': 100.0, 'ch4': 0.03, 'n2o': 1.092, 'unit': 't/TJ'},
        'Naphtha': {'co2': 73.3, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Natural gas': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Other biogas': {'co2': 54.6, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Other Liquid BioFuels': {'co2': 79.6, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Petroleum coke': {'co2': 97.5, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Residual fuel oil': {'co2': 77.4, 'ch4': 0.003, 'n2o': 0.16379999999999997, 'unit': 't/TJ'},
        'Sludge gas': {'co2': 54.6, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Town gas or city gas': {'co2': 56.1, 'ch4': 0.001, 'n2o': 0.0273, 'unit': 't/TJ'},
        'Wood or wood waste': {'co2': 112.0, 'ch4': 0.03, 'n2o': 1.092, 'unit': 't/TJ'},
        'Electricity': {'co2': 0.823, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/MWh'},
        'Hydrogen': {'co2': 0.0, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/TJ'},
    },
    'Transportation (Fuel Sales Approach)': {
        'Petrol': {'co2': 69.3, 'ch4': 0.003, 'n2o': 0.0006, 'unit': 't/TJ'},
        'Diesel': {'co2': 74.1, 'ch4': 0.062, 'n2o': 0.0002, 'unit': 't/TJ'},
        'Auto LPG': {'co2': 56.1, 'ch4': 0.3, 'n2o': 0.004, 'unit': 't/TJ'},
        'Compressed Natural Gas (CNG)': {'co2': 56.1, 'ch4': 0.2, 'n2o': 0.001, 'unit': 't/TJ'},
        'Electricity': {'co2': 0.823, 'ch4': 0.0, 'n2o': 0.0, 'unit': 't/MWh'},
        'Aviation Gasoline': {'co2': 70.0, 'ch4': 0.0005, 'n2o': 0.002, 'unit': 't TJ'},
        'Jet Kerosene': {'co2': 71.5, 'ch4': 0.0005, 'n2o': 0.002, 'unit': 't TJ'},
        'LNG': {'co2': 56.1, 'ch4': 0.01, 'n2o': 0.0006, 'unit': 't TJ'},
    },
}

# ─── Ethanol / Bio-diesel blending shares ─────────────────────────────────
# Each entry: {"fossil_pct": fossil share (0-1), "bio_pct": bio share (0-1)}
ETHANOL_BLENDS = {'G100': {'fossil_pct': 1.0, 'bio_pct': 0.0}, 'E20': {'fossil_pct': 0.8, 'bio_pct': 0.19999999999999996}, 'E25': {'fossil_pct': 0.75, 'bio_pct': 0.25}, 'E27': {'fossil_pct': 0.73, 'bio_pct': 0.27}, 'E30': {'fossil_pct': 0.7, 'bio_pct': 0.30000000000000004}, 'E50': {'fossil_pct': 0.5, 'bio_pct': 0.5}, 'E85': {'fossil_pct': 0.15000000000000002, 'bio_pct': 0.85}, 'B20': {'fossil_pct': 0.8, 'bio_pct': 0.19999999999999996}, 'B25': {'fossil_pct': 0.75, 'bio_pct': 0.25}, 'B27': {'fossil_pct': 0.73, 'bio_pct': 0.27}, 'B30': {'fossil_pct': 0.7, 'bio_pct': 0.30000000000000004}, 'B50': {'fossil_pct': 0.5, 'bio_pct': 0.5}, 'B85': {'fossil_pct': 0.15000000000000002, 'bio_pct': 0.85}, 'SAF10': {'fossil_pct': 0.9, 'bio_pct': 0.09999999999999998}, 'SAF30': {'fossil_pct': 0.7, 'bio_pct': 0.30000000000000004}, 'SAF50': {'fossil_pct': 0.5, 'bio_pct': 0.5}, 'SAF100': {'fossil_pct': 0.0, 'bio_pct': 1.0}}

# ─── Legacy flat-key compatibility map ────────────────────────────────────
# Old app.py used short keys like EF["Res_LPG"]. We map them to the
# (sector, activity) tuples above so existing calc_* functions keep working.
LEGACY_EF_MAP = {
    'Res_Electricity': ('Residential', 'Electricity'),
    'Res_LPG': ('Residential', 'LPG'),
    'Res_Firewood': ('Residential', 'Firewood'),
    'Res_Coal': ('Residential', 'Coal (charcoal)'),
    'Res_PNG': ('Residential', 'PNG/City Gas'),
    'Res_Kerosene': ('Residential', 'Kerosene'),
    'Res_Diesel_Genset': ('Residential', 'Diesel Gen set'),
    'Com_Electricity': ('Commercial', 'Electricity'),
    'Com_LPG': ('Commercial', 'LPG'),
    'Com_PNG': ('Commercial', 'PNG/City Gas'),
    'Com_Firewood': ('Commercial', 'Firewood'),
    'Com_Kerosene': ('Commercial', 'Kerosene'),
    'Ins_Electricity': ('Institutional', 'Electricity'),
    'Ins_LPG': ('Institutional', 'LPG'),
    'Ins_Diesel': ('Institutional', 'Diesel Gen set'),
    'Ind_Electricity': ('Manufacturing', 'Electricity'),
    'Ind_LPG': ('Manufacturing', 'LPG'),
    'Ind_Coal': ('Manufacturing', 'Coal (other bituminous)'),
    'Ind_Diesel': ('Manufacturing', 'Diesel oil'),
    'Ind_PNG': ('Manufacturing', 'Natural gas'),
    'Ind_NatGas': ('Manufacturing', 'Natural gas'),
    'EGen_Coal': ('Energy Industries', 'Coal (other bituminous)'),
    'EGen_NatGas': ('Energy Industries', 'Natural gas'),
    'EGen_Diesel': ('Energy Industries', 'Diesel oil'),
    'EGen_Paraffin': ('Energy Industries', 'Paraffin'),
    'EGen_ResidualOil': ('Energy Industries', 'Residual fuel oil'),
    'Trans_Petrol': ('Transportation (Fuel Sales Approach)', 'Petrol'),
    'Trans_Diesel': ('Transportation (Fuel Sales Approach)', 'Diesel'),
    'Trans_AutoLPG': ('Transportation (Fuel Sales Approach)', 'Auto LPG'),
    'Trans_CNG': ('Transportation (Fuel Sales Approach)', 'Compressed Natural Gas (CNG)'),
    'Trans_Electricity': ('Transportation (Fuel Sales Approach)', 'Electricity'),
    'Trans_AvGasoline': ('Transportation (Fuel Sales Approach)', 'Aviation Gasoline'),
    'Trans_JetKerosene': ('Transportation (Fuel Sales Approach)', 'Jet Kerosene'),
    'Trans_LNG': ('Transportation (Fuel Sales Approach)', 'LNG'),
}

# Hand-tuned aliases for activities not present in the EF sheet directly
# (e.g., Railway uses Trans_Diesel's row, EV cars use Trans_Electricity's).
EF = {}
for _k, (_s, _a) in LEGACY_EF_MAP.items():
    _table = EF_BY_SECTOR.get(_s, {}).get(_a)
    if _table is not None:
        EF[_k] = dict(_table)

# Additional transport rows used by app.py that map to the same row as a parent
_RAILWAY_ALIASES = {
    "Trans_Railway_Die": "Trans_Diesel",
    "Trans_Railway_Ele": "Trans_Electricity",
    "Trans_Water_Die":   "Trans_Diesel",
    "Trans_Water_Pet":   "Trans_Petrol",
    "Trans_Hydrogen":    None,  # zero-EF
    "Trans_Lubricants":  None,  # use Manufacturing Lubricants below
}
for _new, _parent in _RAILWAY_ALIASES.items():
    if _parent and _parent in EF:
        EF[_new] = dict(EF[_parent])
    elif _new == "Trans_Hydrogen":
        EF[_new] = {"co2": 0.0, "ch4": 0.0, "n2o": 0.0, "unit": "t/TJ"}
    elif _new == "Trans_Lubricants":
        _src = EF_BY_SECTOR.get("Manufacturing", {}).get("Lubricants")
        if _src: EF[_new] = dict(_src)

# Volumetric conversion shortcuts kept on the EF row for legacy compatibility.
# (Authoritative table lives in data/conv_factors.py — these are caches.)
_LEGACY_CONV = {
    'Trans_Petrol': ('conv_kl', 0.034839687),
    'Trans_Diesel': ('conv_kl', 0.038492544),
    'Trans_AutoLPG': ('conv_t', 0.0473),
    'Trans_CNG': ('conv_t', 0.048),
    'Trans_LNG': ('conv_t', 0.048),
    'Trans_AvGasoline': ('conv_kl', 0.0334461),
    'Trans_JetKerosene': ('conv_kl', 0.37626862),
    'Trans_Railway_Die': ('conv_kl', 0.038492544),
    'Trans_Water_Die': ('conv_kl', 0.038492544),
    'Trans_Water_Pet': ('conv_kl', 0.034839687),
    'Trans_Lubricants': ('conv_kl', 0.034),
}
for _k, (_attr, _v) in _LEGACY_CONV.items():
    if _k in EF:
        EF[_k][_attr] = _v


def get_ef(sector, activity):
    """Look up an EF row by sector + activity name."""
    return EF_BY_SECTOR.get(sector, {}).get(activity)

"""
Physical unit conversion tables — volume, mass, SI prefixes.
Extracted from "Cost and Conversion Factor" sheet (rows 10-39).

For fuel→TJ conversions (the bulk of the workbook's conversion logic),
see data/conv_factors.py — those are kept in the existing module untouched.
"""

# ─── Volume conversion (multiply: from-unit × table[to-unit] = to-unit value) ─
VOLUME_FROM_TO = {
    "l": {
        "l": 1.0,
        "m3": 0.001,
        "ft3": 0.0353,
        "bbl": 0.0063,
        "UK gal": 0.22,
        "US gal": 0.2642007926023778
    },
    "m3": {
        "l": 1000.0,
        "m3": 1.0,
        "ft3": 35.3,
        "bbl": 6.3,
        "UK gal": 220.0,
        "US gal": 264.20079260237776
    },
    "ft3": {
        "l": 28.3,
        "m3": 0.0283,
        "ft3": 1.0,
        "bbl": 0.1781,
        "UK gal": 6.229,
        "US gal": 7.48
    },
    "bbl": {
        "l": 159.0,
        "m3": 0.159,
        "ft3": 5.615,
        "bbl": 1.0,
        "UK gal": 34.97,
        "US gal": 42.0
    },
    "gal": {
        "l": 3.785,
        "m3": 0.0038,
        "ft3": 0.1337,
        "bbl": 0.02381,
        "UK gal": 0.8327,
        "US gal": 1.0
    }
}

# ─── Mass conversion ────────────────────────────────────────────────────────
MASS_FROM_TO = {
    "g": {
        "g": 1.0,
        "kg": 0.001,
        "t": 1e-06,
        "kt": 1e-09,
        "lt": 9.84e-07,
        "st": 1.102e-06,
        "lb": 0.0022046
    },
    "kg": {
        "g": 1000.0,
        "kg": 1.0,
        "t": 0.001,
        "kt": 1e-06,
        "lt": 0.000984,
        "st": 0.001102,
        "lb": 2.2046
    },
    "t": {
        "g": 1000000.0,
        "kg": 1000.0,
        "t": 1.0,
        "kt": 0.001,
        "lt": 0.984,
        "st": 1.1023,
        "lb": 2204.6
    },
    "kt": {
        "g": 1000000000.0,
        "kg": 1000000.0,
        "t": 1000.0,
        "kt": 1.0,
        "lt": 984.0,
        "st": 1102.3,
        "lb": 2204600.0
    },
    "lt": {
        "g": 1016000.0,
        "kg": 1016.0,
        "t": 1.016,
        "kt": 0.0010162601626016261,
        "lt": 1.0,
        "st": 1.12,
        "lb": 2240.0
    },
    "st": {
        "g": 907200.0,
        "kg": 907.2,
        "t": 0.9072,
        "kt": 0.0009071940488070398,
        "lt": 0.893,
        "st": 1.0,
        "lb": 2000.0
    },
    "lb": {
        "g": 453.5970244035199,
        "kg": 0.4535970244035199,
        "t": 0.0004535970244035199,
        "kt": 4.535970244035199e-07,
        "lt": 0.0004464285714285714,
        "st": 0.0005,
        "lb": 1.0
    }
}

# ─── SI prefix multipliers (Tera, Giga, Mega, Kilo) ─────────────────────────
SI_PREFIX = {
    "tera": {
        "T": 1.0,
        "G": 1000.0,
        "M": 1000000.0,
        "k": 1000000000.0
    },
    "giga": {
        "T": 0.001,
        "G": 1.0,
        "M": 1000.0,
        "k": 1000000.0
    },
    "mega": {
        "T": 1e-06,
        "G": 0.001,
        "M": 1.0,
        "k": 1000.0
    },
    "kilo": {
        "T": 1e-09,
        "G": 1e-06,
        "M": 0.001,
        "k": 1.0
    }
}


def convert_volume(value, from_unit, to_unit):
    """Convert a volume between any two units in VOLUME_FROM_TO."""
    row = VOLUME_FROM_TO.get(from_unit.lower())
    if row is None: return None
    factor = row.get(to_unit.lower())
    return None if factor is None else float(value) * factor


def convert_mass(value, from_unit, to_unit):
    """Convert a mass between any two units in MASS_FROM_TO."""
    row = MASS_FROM_TO.get(from_unit.lower())
    if row is None: return None
    factor = row.get(to_unit.lower())
    return None if factor is None else float(value) * factor

# ─── App-level fuel→TJ shortcuts (legacy compatibility with app.py) ─────────
# This is the short-key view of the conversion table the calc_* functions use.
# Authoritative table: data/conv_factors.py CONV_FACTORS (keyed by (fuel,unit) tuple)
FUEL_CONV = {
    "Petrol":      {"kl_to_tj": 0.034839687},
    "Diesel":      {"kl_to_tj": 0.038492544},
    "AutoLPG":     {"t_to_tj":  0.0383791509},
    "CNG":         {"t_to_tj":  0.048},
    "LPG":         {"t_to_tj":  0.0473},
    "PNG":         {"t_to_tj":  0.038379151},
    "Firewood":    {"t_to_tj":  0.020329320},
    "Coal":        {"t_to_tj":  0.029051584},
    "Kerosene":    {"kl_to_tj": 0.037630000},
    "NatGas":      {"t_to_tj":  0.048},
    "AvGasoline":  {"kl_to_tj": 0.0334461},
    "JetKerosene": {"kl_to_tj": 0.37626862},
    "LNG":         {"t_to_tj":  0.048},
    "Lubricants":  {"kl_to_tj": 0.034},
    "Hydrogen":    {"kg_to_tj": 0.12},
}

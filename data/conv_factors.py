# ─── Conversion Factors: ANY fuel × ANY unit → TJ ──────────────────────────────
# Built from the EF_Sources / ListsAndTables conversion table.
# Keys are case-insensitive; lookups go through `tj_factor()` which lowercases.
# Factor units: 1 unit-of-fuel × FACTOR = TJ
CONV_FACTORS = {
    # fuel name (lowercase)            unit (lowercase)        factor (× to TJ)
    ("auto lpg",                        "kg"):                  0.000038379150866228,
    ("auto lpg",                        "tonne"):               0.038379150866228200,
    ("auto lpg",                        "m3"):                  0.025642009716252700,
    ("aviation gasoline",               "l"):                   0.000033446099629895,
    ("aviation gasoline",               "kl"):                  0.033446099629894800,
    ("aviation gasoline",               "m3"):                  0.033446099629894800,
    ("biodiesels",                      "kl"):                  0.035675840000000000,
    ("biogasoline",                     "kl"):                  0.027000000000000000,
    ("bitumen",                         "tonne"):               0.040200000000000000,
    ("butane",                          "m3"):                  0.028707902000000000,
    ("coal (charcoal)",                 "kg"):                  0.000029051854201163,
    ("coal (charcoal)",                 "tonne"):               0.029051854201163000,
    ("coal (lignite)",                  "tonne"):               0.029051584000000000,
    ("coal (other bituminous)",         "tonne"):               0.029051584000000000,
    ("coal (sub - bituminous)",         "tonne"):               0.029051584000000000,
    ("coke",                            "tonne"):               0.027000000000000000,
    ("coking coal",                     "tonne"):               0.028842513000000000,
    ("compressed natural gas (cng)",    "tonne"):               0.048000000000000000,
    ("compressed natural gas (cng)",    "scm"):                 0.000038294527952752,
    ("compressed natural gas (cng)",    "m3"):                  3.829450000000000000,
    ("crude oil",                       "kl"):                  0.038463015000000000,
    ("diesel gen set",                  "kl"):                  0.038490000000000000,
    ("diesel gen set",                  "m3"):                  0.038490000000000000,
    ("diesel oil",                      "kl"):                  0.038492544000000000,
    ("e10",                             "kl"):                  0.034200000000000000,
    ("e15",                             "kl"):                  0.032800000000000000,
    ("e30",                             "kl"):                  0.029000000000000000,
    ("e85",                             "kl"):                  0.025000000000000000,
    ("electricity",                     "kwh"):                 0.001000000000000000 * 0.0036,  # kWh → GJ→TJ (note below)
    ("electricity",                     "mwh"):                 0.0036,                          # 1 MWh = 0.0036 TJ
    ("ethanol",                         "kl"):                  0.023412270000000000,
    ("firewood",                        "kg"):                  0.000020329319913384,
    ("firewood",                        "tonne"):               0.020329319913383900,
    ("gas oil",                         "kl"):                  0.038908963000000000,
    ("hydrogen",                        "m3"):                  0.000010800000000000,            # ≈ 10.8 MJ/m³
    ("jet gasoline",                    "kl"):                  0.033446100000000000,
    ("jet kerosene",                    "kl"):                  0.376268620000000000,
    ("kerosene",                        "l"):                   0.000037630000000000,
    ("kerosene",                        "kl"):                  0.037630000000000000,
    ("kerosene",                        "m3"):                  0.037630000000000000,
    ("paraffin",                        "kl"):                  0.376268620000000000,
    ("landfill gas",                    "m3"):                  0.000050660000000000,
    ("liqu. natural gas",               "kg"):                  0.000027400000000000,
    ("liqu. natural gas",               "tonne"):               0.027400000000000000,
    ("liqu. natural gas",               "m3"):                  0.025642009716252700,
    ("liquefied natural gas (lng)",     "m3"):                  0.023640818000000000,
    ("liquefied petroleum gas (lpg)",   "kl"):                  0.025642010000000000,
    ("lpg",                             "kg"):                  0.000047300000000000,
    ("lpg",                             "tonne"):               0.047300000000000000,
    ("lpg",                             "scm"):                 0.025642009716252700,
    ("lubricants",                      "kl"):                  0.040135320000000000,
    ("methanol",                        "kl"):                  0.018172381000000000,
    ("motor gasoline (petrol)",         "kl"):                  0.034839687000000000,
    ("municipal wastes (all)",          "tonne"):               0.011571895000000000,
    ("municipal wastes (biomass fraction)",     "tonne"):       0.012909351000000000,
    ("municipal wastes (non-biomass fraction)", "tonne"):       0.026749105000000000,
    ("naphtha",                         "kl"):                  0.034839668700000000,
    ("natural gas",                     "m3"):                  0.000038257200000000,            # ≈ 38.257 MJ/m³
    ("natural gas",                     "tonne"):               0.048000000000000000,
    ("other biogas",                    "m3"):                  0.000024404700000000,
    ("other liquid biofuels",           "kl"):                  0.027400000000000000,
    ("petrol",                          "kl"):                  0.034839687114473700,
    ("petrol",                          "m3"):                  0.034839687114473700,
    ("petroleum coke",                  "tonne"):               0.032500000000000000,
    ("png/city gas",                    "kg"):                  0.000038379150866228,
    ("png/city gas",                    "tonne"):               0.038379150866228200,
    ("png/city gas",                    "mmbtu"):               0.001055000000000000,
    ("png/city gas",                    "scm"):                 0.000038520000000000,
    ("propane",                         "m3"):                  0.025363292000000000,
    ("residual fuel oil",               "kl"):                  0.040414037000000000,
    ("residue fuel oil",                "m3"):                  0.040410000000000000,
    ("sewage sludge",                   "tonne"):               0.003800000000000000,
    ("sludge gas",                      "m3"):                  0.000023137900000000,
    ("town gas or city gas",            "tonne"):               0.038379151000000000,
    ("town gas or city gas",            "m3"):                  0.000038520000000000,
    ("wood or wood waste",              "tonne"):               0.020329320000000000,
    ("anthracite",                      "tonne"):               0.026700000000000000,
    # Convenience aliases (so existing form names also resolve)
    ("firewood",                        "kg"):                  0.000020329319913384,
    ("coal",                            "tonne"):               0.029051584000000000,
    ("diesel",                          "kl"):                  0.038492544000000000,
    ("png",                             "tonne"):               0.038379151000000000,
}

# Map of generic emission-factor keys for any fuel name. CO2 / CH4 / N2O in t/TJ.
# Used for the new tabs (Mfg, Energy Industries) where the user picks any fuel.
GENERIC_FUEL_EF = {
    "lpg":                                  {"co2": 63.1,  "ch4": 0.005, "n2o": 0.0001},
    "biodiesels":                           {"co2": 70.8,  "ch4": 0.003, "n2o": 0.0006},
    "biogasoline":                          {"co2": 70.8,  "ch4": 0.003, "n2o": 0.0006},
    "bitumen":                              {"co2": 80.7,  "ch4": 0.003, "n2o": 0.0006},
    "coal (charcoal)":                      {"co2": 112.0, "ch4": 0.2,   "n2o": 0.001},
    "coal (other bituminous)":              {"co2": 94.6,  "ch4": 0.01,  "n2o": 0.0015},
    "coal (sub - bituminous)":              {"co2": 96.1,  "ch4": 0.01,  "n2o": 0.0015},
    "coal (lignite)":                       {"co2": 101.0, "ch4": 0.01,  "n2o": 0.0015},
    "coke":                                 {"co2": 107.0, "ch4": 0.01,  "n2o": 0.0015},
    "coking coal":                          {"co2": 94.6,  "ch4": 0.01,  "n2o": 0.0015},
    "anthracite":                           {"co2": 98.3,  "ch4": 0.01,  "n2o": 0.0015},
    "compressed natural gas (cng)":         {"co2": 56.1,  "ch4": 0.005, "n2o": 0.0001},
    "diesel oil":                           {"co2": 74.1,  "ch4": 0.003, "n2o": 0.0006},
    "ethanol":                              {"co2": 70.8,  "ch4": 0.003, "n2o": 0.0006},
    "gas oil":                              {"co2": 74.1,  "ch4": 0.003, "n2o": 0.0006},
    "paraffin":                             {"co2": 71.9,  "ch4": 0.003, "n2o": 0.0006},
    "liquefied natural gas (lng)":          {"co2": 56.1,  "ch4": 0.005, "n2o": 0.0001},
    "lubricants":                           {"co2": 73.3,  "ch4": 0.003, "n2o": 0.0006},
    "municipal wastes (non-biomass fraction)": {"co2": 91.7, "ch4": 0.03, "n2o": 0.004},
    "municipal wastes (biomass fraction)":  {"co2": 0.0,   "ch4": 0.03,  "n2o": 0.004},
    "naphtha":                              {"co2": 73.3,  "ch4": 0.003, "n2o": 0.0006},
    "natural gas":                          {"co2": 56.1,  "ch4": 0.005, "n2o": 0.0001},
    "other biogas":                         {"co2": 0.0,   "ch4": 0.005, "n2o": 0.0001},
    "other liquid biofuels":                {"co2": 79.6,  "ch4": 0.003, "n2o": 0.0006},
    "petroleum coke":                       {"co2": 97.5,  "ch4": 0.003, "n2o": 0.0006},
    "residual fuel oil":                    {"co2": 77.4,  "ch4": 0.003, "n2o": 0.0006},
    "sludge gas":                           {"co2": 0.0,   "ch4": 0.005, "n2o": 0.0001},
    "town gas or city gas":                 {"co2": 44.4,  "ch4": 0.005, "n2o": 0.0001},
    "wood or wood waste":                   {"co2": 112.0, "ch4": 0.3,   "n2o": 0.004},
    "electricity":                          {"co2": 0.82,  "ch4": 0.0,   "n2o": 0.0, "elec": True},
    "hydrogen":                             {"co2": 0.0,   "ch4": 0.0,   "n2o": 0.0},
    # Aliases
    "firewood":                             {"co2": 112.0, "ch4": 0.3,   "n2o": 0.004},
    "png/city gas":                         {"co2": 44.4,  "ch4": 0.005, "n2o": 0.0001},
    "kerosene":                             {"co2": 71.9,  "ch4": 0.003, "n2o": 0.0006},
    "diesel gen set":                       {"co2": 74.1,  "ch4": 0.003, "n2o": 0.0006},
}


def tj_factor(fuel_name, unit):
    """Return the multiplier that converts 1 unit of fuel into TJ. Returns 0.0 if unknown."""
    if not fuel_name or not unit:
        return 0.0
    key = (str(fuel_name).strip().lower(), str(unit).strip().lower())
    return CONV_FACTORS.get(key, 0.0)


def emit_for_fuel(value, unit, fuel_name, gwp_ch4=29.8, gwp_n2o=273.0):
    """
    Convert a raw fuel input (value, unit) into tCO2e using generic EFs.
    For electricity: value (MWh) × CO2_per_MWh
    For everything else: value × tj_factor → TJ × (CO2 + CH4·GWP + N2O·GWP)
    """
    try:
        v = float(value or 0)
    except (TypeError, ValueError):
        return 0.0
    if v <= 0:
        return 0.0
    ef = GENERIC_FUEL_EF.get(str(fuel_name).strip().lower())
    if not ef:
        return 0.0
    if ef.get("elec"):
        # Electricity is special — treat MWh directly
        if str(unit).strip().lower() == "mwh":
            return v * ef["co2"]
        if str(unit).strip().lower() == "kwh":
            return (v / 1000.0) * ef["co2"]
        return 0.0
    tj = v * tj_factor(fuel_name, unit)
    return tj * (ef["co2"] + ef["ch4"] * gwp_ch4 + ef["n2o"] * gwp_n2o)

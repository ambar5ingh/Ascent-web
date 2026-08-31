"""
Decarbonisation strategies + cost tables.
Extracted from "Cost and Conversion Factor" and "Stratergies & Cost" sheets.
"""

# ─── FX rates (Cost sheet r48-49) ───────────────────────────────────────────
FX_RATES = {'USD_INR': 91.928, 'EUR_INR': 106.802}

# ─── Sector-level abatement cost (₹/tCO2e reduced) ──────────────────────────
# These are weighted averages used by calc_mitigation_budget(). The detailed
# action-level costs are in DECARB_COSTS below.
ABATEMENT_COST = {'Buildings': 2500, 'Transport': 3200, 'Waste': 1800, 'Wastewater': 1500, 'AFOLU': 800, 'IPPU': 4500}

# ─── Fuel cost per kWh (Cost sheet r54-106) ─────────────────────────────────
FUEL_COSTS = [
    {
        "fuel": "Aviation gasoline",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 9.291
    },
    {
        "fuel": "Biodiesel",
        "subsector": "NA",
        "cost_inr": 90.0,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 9.91
    },
    {
        "fuel": "Biogasoline",
        "subsector": "NA",
        "cost_inr": 25.0,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 8.98
    },
    {
        "fuel": "Bitumen",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 11.167
    },
    {
        "fuel": "Butane",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 7.974
    },
    {
        "fuel": "Charcoal",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 8.194
    },
    {
        "fuel": "Coal (Bituminous or Black coal)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 8.07
    },
    {
        "fuel": "Coal (manufactured solid fuels)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "cubic meter",
        "dest_unit": "kWh",
        "to_kwh": 5756.161
    },
    {
        "fuel": "Coke",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 7.5
    },
    {
        "fuel": "Coking coal",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 8.012
    },
    {
        "fuel": "Compressed Natural Gas (CNG)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "cubic meter",
        "dest_unit": "kWh",
        "to_kwh": 10.637
    },
    {
        "fuel": "Crude oil",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "bbl",
        "dest_unit": "kWh",
        "to_kwh": 1698.049
    },
    {
        "fuel": "Diesel oil",
        "subsector": "NA",
        "cost_inr": 98.0,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 10.691
    },
    {
        "fuel": "E85 (Flex Fuel)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 7.111
    },
    {
        "fuel": "Electricity",
        "subsector": "Residential",
        "cost_inr": 8.0,
        "cost_usd": None,
        "source_unit": "kWh",
        "dest_unit": "kWh",
        "to_kwh": 0.81
    },
    {
        "fuel": "Electricity",
        "subsector": "Commercial",
        "cost_inr": 15.0,
        "cost_usd": None,
        "source_unit": "kWh",
        "dest_unit": "kWh",
        "to_kwh": 0.81
    },
    {
        "fuel": "Electricity",
        "subsector": "Insititutional",
        "cost_inr": 12.0,
        "cost_usd": None,
        "source_unit": "kWh",
        "dest_unit": "kWh",
        "to_kwh": 0.81
    },
    {
        "fuel": "Electricity",
        "subsector": "Manufacturing & Construction",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "kWh",
        "dest_unit": "kWh",
        "to_kwh": 0.81
    },
    {
        "fuel": "Electricity",
        "subsector": "Others",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "kWh",
        "dest_unit": "kWh",
        "to_kwh": 0.81
    },
    {
        "fuel": "Ethanol",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 6.503
    },
    {
        "fuel": "Hydrogen (Used for Vehicle)",
        "subsector": "NA",
        "cost_inr": 170.0,
        "cost_usd": None,
        "source_unit": "bbl",
        "dest_unit": "kWh",
        "to_kwh": 1717.737
    },
    {
        "fuel": "Geothermal",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "kWh",
        "dest_unit": "kWh",
        "to_kwh": 1.0
    },
    {
        "fuel": "Hydrogen (Used for Vehicle)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 9.678
    },
    {
        "fuel": "Jet gasoline",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 9.291
    },
    {
        "fuel": "Jet kerosene",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 10.452
    },
    {
        "fuel": "Kerosene",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 10.452
    },
    {
        "fuel": "landfill gas",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "cubic meter",
        "dest_unit": "kWh",
        "to_kwh": 5.02
    },
    {
        "fuel": "Liquefied Natural Gas (LNG)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 6.566
    },
    {
        "fuel": "Liquefied Petroleum Gas (LPG)",
        "subsector": "Residential",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 7.123
    },
    {
        "fuel": "Liquefied Petroleum Gas (LPG)",
        "subsector": "Commercial",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 7.123
    },
    {
        "fuel": "Liquefied Petroleum Gas (LPG)",
        "subsector": "Insititutional",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 7.123
    },
    {
        "fuel": "Liquefied Petroleum Gas (LPG)",
        "subsector": "Manufacturing & Construction",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 7.123
    },
    {
        "fuel": "lubricants",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": None,
        "dest_unit": "kWh",
        "to_kwh": 11.149
    },
    {
        "fuel": "Methanol",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 5.048
    },
    {
        "fuel": "Methane",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "MMBtu",
        "dest_unit": "kWh",
        "to_kwh": 293.297
    },
    {
        "fuel": "Petrol",
        "subsector": "NA",
        "cost_inr": 100.0,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 9.678
    },
    {
        "fuel": "Municipal wastes (all)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 3.214
    },
    {
        "fuel": "Municipal wastes (biomass fraction)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 3.585
    },
    {
        "fuel": "Municipal wastes (non-biomass fraction)",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 7.43
    },
    {
        "fuel": "Naphtha",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 9.678
    },
    {
        "fuel": "Other biogas",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "cubic meter",
        "dest_unit": "kWh",
        "to_kwh": 6.779
    },
    {
        "fuel": "Otherliquid BioFuels",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 9.445
    },
    {
        "fuel": "Petroleum coke",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 9.028
    },
    {
        "fuel": "PNG/City Gas",
        "subsector": "Residential",
        "cost_inr": 75.0,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 10.66
    },
    {
        "fuel": "PNG/City Gas",
        "subsector": "Commercial",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 10.66
    },
    {
        "fuel": "PNG/City Gas",
        "subsector": "Insititutional",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 10.66
    },
    {
        "fuel": "PNG/City Gas",
        "subsector": "Manufacturing & Construction",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 10.66
    },
    {
        "fuel": "Propane",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 7.045
    },
    {
        "fuel": "Residual fuel oil",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "l",
        "dest_unit": "kWh",
        "to_kwh": 11.226
    },
    {
        "fuel": "Sewage sludge",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 1.056
    },
    {
        "fuel": "Sludge gas",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "cubic meter",
        "dest_unit": "kWh",
        "to_kwh": 6.427
    },
    {
        "fuel": "Wood or wood waste",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "Kg",
        "dest_unit": "kWh",
        "to_kwh": 5.647
    },
    {
        "fuel": "Nuclear",
        "subsector": "NA",
        "cost_inr": None,
        "cost_usd": None,
        "source_unit": "kWh",
        "dest_unit": "kWh",
        "to_kwh": 1.0
    }
]

# ─── Decarbonisation actions with cost (Cost sheet r112-250) ────────────────
DECARB_COSTS = [
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Clinker to cement ratio",
        "action": "blast furnace slag",
        "cost": 4000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Clinker to cement ratio",
        "action": "fly ash",
        "cost": 3000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Clinker to cement ratio",
        "action": "natural pozzolanas",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Clinker to cement ratio",
        "action": "calcined clay",
        "cost": 25.0,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Clinker to cement ratio",
        "action": "calcined clay with limestone",
        "cost": 25.0,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "CCS",
        "action": "CSS-direct separation",
        "cost": 37.0,
        "currency": "€",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "CCS",
        "action": "CCS—advanced amines",
        "cost": 40.0,
        "currency": "$",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "CCS",
        "action": "CCS—calcium looping",
        "cost": 30.0,
        "currency": "$",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "CCS",
        "action": "CCS—molten carbonate fuel cell",
        "cost": 33.63,
        "currency": "$",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "CCS",
        "action": "CCS—partial oxyfuel",
        "cost": 42.0,
        "currency": "€",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Cement kiln",
        "action": "fuel switching—biomass/waste",
        "cost": None,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Cement kiln",
        "action": "fuel switching—hydrogen",
        "cost": 1559.0,
        "currency": "€",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Cement kiln",
        "action": "plasma torches—electricity",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Cement kiln",
        "action": "Low pressure drop cyclone",
        "cost": 13.5,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Cement",
        "process": "Cement kiln",
        "action": "Cyclone preheater and precalciner",
        "cost": 263.0,
        "currency": "€",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime production",
        "action": "chemical synthesis",
        "cost": None,
        "currency": "€",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime production",
        "action": "electrochemical synthesis",
        "cost": 0.0,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime CCS",
        "action": "CCS—direct separation",
        "cost": 50.0,
        "currency": "€",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime CCS",
        "action": "CCS—advanced amines",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime CCS",
        "action": "CCS—calcium looping",
        "cost": 59.0,
        "currency": "€",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime CCS",
        "action": "CCS—MCFC",
        "cost": 33.63,
        "currency": "$",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime CCS",
        "action": "CCS—partial oxyfuel",
        "cost": 42.0,
        "currency": "€",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime kiln",
        "action": "fuel switching—biomass/waste",
        "cost": None,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime kiln",
        "action": "fuel switching—hydrogen",
        "cost": 1559.0,
        "currency": "$",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime kiln",
        "action": "plasma torches—electricity",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Lime",
        "process": "Lime kiln",
        "action": "kiln upgrade",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "electric furnace",
        "cost": 1000000.0,
        "currency": "₹",
        "unit": None
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "plasma melting",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "hybrid furnace",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "fuel switching—biofuel",
        "cost": 28000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "fuel switching—hydrogen",
        "cost": 330000.0,
        "currency": "₹",
        "unit": "Per tonne of H2"
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "oxy-fuel furnace",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "increased cullet use",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Glass",
        "process": "Glass Production (glass furnace)",
        "action": "calcined raw materials",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Natural gas-based ammonia synthesis",
        "action": "blue hydrogen production + ammonia synthesis",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Natural gas-based ammonia synthesis",
        "action": "green hydrogen production + ammonia synthesis",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Natural gas-based ammonia synthesis",
        "action": "biomass gasification/ digestion + ammonia synthesis",
        "cost": None,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Natural gas-based ammonia synthesis",
        "action": "methane pyrolysis + ammonia synthesis",
        "cost": 187.0,
        "currency": "$",
        "unit": "Per tonne of Ammonia"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam cracker",
        "action": "CCS",
        "cost": 771.0,
        "currency": "$",
        "unit": "Per tonne of Ethylene"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam cracker",
        "action": "electric steam cracker",
        "cost": 800.0,
        "currency": "$",
        "unit": "Per tonne of Ethylene"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam cracker",
        "action": "hydrogen fuel switching for steam cracker",
        "cost": 330000.0,
        "currency": "₹",
        "unit": "Per tonne of H2"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam cracker",
        "action": "alternative feedstock for steam cracker (bio-naphtha 10 wt %)",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam cracker",
        "action": "methanol to olefins (MTO) and to aromatics",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam reforming— hydrogen and methanol",
        "action": "AEL/PEM electrolyzer",
        "cost": 6000.0,
        "currency": "$",
        "unit": "Per tonne H2"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam reforming— hydrogen and methanol",
        "action": "solid oxide electrolyzer",
        "cost": 2419.0,
        "currency": "€",
        "unit": "Per tonne of methonal"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam reforming— hydrogen and methanol",
        "action": "CCS",
        "cost": 100.0,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Chemicals",
        "process": "Steam reforming— hydrogen and methanol",
        "action": "biomass/waste gasification",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "Process heat (furnaces)",
        "action": "fuel switching—hydrogen",
        "cost": 330000.0,
        "currency": "₹",
        "unit": "Per tonne of H2"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "Process heat (furnaces)",
        "action": "furnaces electrification",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "Process heat (furnaces)",
        "action": "CCS",
        "cost": 7500.0,
        "currency": "₹",
        "unit": "Per tonne of CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "CHP and steam boilers",
        "action": "fuel switching— biomass",
        "cost": 28000.0,
        "currency": "₹",
        "unit": "Per tonne of biomass"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "CHP and steam boilers",
        "action": "fuel switching— hydrogen",
        "cost": 330000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "CHP and steam boilers",
        "action": "fuel cells",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "CHP and steam boilers",
        "action": "electric boiler",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "CHP and steam boilers",
        "action": "biomass boiler",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "CHP and steam boilers",
        "action": "hydrogen boiler",
        "cost": 60000.0,
        "currency": "€",
        "unit": "5 MW boiler"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "Steam reforming (process emissions)",
        "action": "AEL/PEM electrolyzer",
        "cost": 400.0,
        "currency": "$",
        "unit": "Per kW"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "Steam reforming (process emissions)",
        "action": "solid oxide electrolyzer",
        "cost": 1125.0,
        "currency": "$",
        "unit": "Per kW"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "Steam reforming (process emissions)",
        "action": "CCS",
        "cost": 100.0,
        "currency": "$",
        "unit": "Per tonne CO2"
    },
    {
        "sector": "IPPU",
        "subsector": "Petrochemicals",
        "process": "Steam reforming (process emissions)",
        "action": "biomass/waste gasification",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Iron and Steel",
        "process": "Primary iron and steel",
        "action": "hydrogen direct reduction - shaft furnace + EAF",
        "cost": 490.0,
        "currency": "€",
        "unit": "Per tonne of crude steel"
    },
    {
        "sector": "IPPU",
        "subsector": "Iron and Steel",
        "process": "Primary iron and steel",
        "action": "smelting reduction (HIsarna) + CCS",
        "cost": 520.0,
        "currency": "€",
        "unit": "Per tonne of crude steel"
    },
    {
        "sector": "IPPU",
        "subsector": "Iron and Steel",
        "process": "Primary iron and steel",
        "action": "hydrogen-based flash reactor",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Iron and Steel",
        "process": "Primary iron and steel",
        "action": "biomass fuel substitution to coal/coke use",
        "cost": 28000.0,
        "currency": "₹",
        "unit": "Per tonne of biomass"
    },
    {
        "sector": "IPPU",
        "subsector": "Iron and Steel",
        "process": "Primary iron and steel",
        "action": "electric arc furnace",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Iron and Steel",
        "process": "Primary iron and steel",
        "action": "CCS",
        "cost": 4000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Aluminum",
        "process": "Aluminum",
        "action": "low-carbon electricity",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Aluminum",
        "process": "steam boiler",
        "action": "electric boiler",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Aluminum",
        "process": "steam boiler",
        "action": "biomass boiler",
        "cost": 6993.0,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Aluminum",
        "process": "steam boiler",
        "action": "hydrogen boiler",
        "cost": 3000.0,
        "currency": "€",
        "unit": "Per tonne"
    },
    {
        "sector": "IPPU",
        "subsector": "Aluminum",
        "process": "steam boiler",
        "action": "heat pump",
        "cost": 6000.0,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Inhibitors",
        "action": "Nitrooxypropanol",
        "cost": None,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Electron receptors",
        "action": "Nitrate",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Electron receptors",
        "action": "Fumaric acid",
        "cost": 3922.275782,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Ionophores",
        "action": "Monensin",
        "cost": 490000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Plant bioactive compounds",
        "action": "Shorghum seed",
        "cost": 10000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Plant bioactive compounds",
        "action": "Sheanut",
        "cost": 1100.0,
        "currency": "₹",
        "unit": "Per kg"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Plant bioactive compounds",
        "action": "Wakame seaweed",
        "cost": 1500.0,
        "currency": "₹",
        "unit": "Per kg"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Plant bioactive compounds",
        "action": "Hijiki Seaweed",
        "cost": 575.0,
        "currency": "₹",
        "unit": "Per kg"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Plant bioactive compounds",
        "action": "Arame Seaweed",
        "cost": 669.0,
        "currency": "₹",
        "unit": "Per kg"
    },
    {
        "sector": "AFOLU",
        "subsector": "Enteric Fermentation",
        "process": "Plant bioactive compounds",
        "action": "Essential oil",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Manure Management",
        "process": None,
        "action": "Anaerobic Treatment",
        "cost": 5000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Manure Management",
        "process": None,
        "action": "Composting",
        "cost": 500.0,
        "currency": "$",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Manure Management",
        "process": None,
        "action": "Community Biogas Plant",
        "cost": 5000.0,
        "currency": "₹",
        "unit": "Per tonne"
    },
    {
        "sector": "AFOLU",
        "subsector": "Forest Land",
        "process": None,
        "action": "Aforestation",
        "cost": 800000.0,
        "currency": "₹",
        "unit": "Per Hectare"
    },
    {
        "sector": "AFOLU",
        "subsector": "Forest Land",
        "process": None,
        "action": "Reforestation",
        "cost": 52.0,
        "currency": "$",
        "unit": "Per Hectare"
    },
    {
        "sector": "AFOLU",
        "subsector": "Cropland",
        "process": None,
        "action": "Cropland",
        "cost": 1500.0,
        "currency": "$",
        "unit": "Per Hectare"
    },
    {
        "sector": "AFOLU",
        "subsector": "Grass Land",
        "process": None,
        "action": "Grass Land",
        "cost": 56000.0,
        "currency": "₹",
        "unit": "Per Hectare"
    },
    {
        "sector": "AFOLU",
        "subsector": "Setlements",
        "process": None,
        "action": "Setlements",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per Hectare"
    },
    {
        "sector": "AFOLU",
        "subsector": "Other Lands",
        "process": None,
        "action": "Other Lands",
        "cost": 0.0,
        "currency": "₹",
        "unit": "Per Hectare"
    },
    {
        "sector": "Waste",
        "subsector": None,
        "process": None,
        "action": "Anerobic Digestor with Biogass Capture",
        "cost": 1276.53202,
        "currency": "$",
        "unit": "Mbtu"
    },
    {
        "sector": "Waste",
        "subsector": None,
        "process": None,
        "action": "Anerobic Digestor without Biogass Capture",
        "cost": 0.0,
        "currency": "₹",
        "unit": None
    },
    {
        "sector": "Waste",
        "subsector": None,
        "process": None,
        "action": "Lanfill Methane Gas Capture Rate",
        "cost": 167960.1377,
        "currency": "$",
        "unit": "Per kW"
    },
    {
        "sector": "Renewable energy",
        "subsector": None,
        "process": None,
        "action": "Solar PLV",
        "cost": 50000.0,
        "currency": "₹",
        "unit": "Per Kw"
    },
    {
        "sector": "Renewable energy",
        "subsector": None,
        "process": None,
        "action": "Wind TurbinesOff Shore",
        "cost": 262301100.0,
        "currency": "$",
        "unit": "Per Wind turbine ("
    },
    {
        "sector": "Renewable energy",
        "subsector": None,
        "process": None,
        "action": "Wind Turbines On Shore",
        "cost": 174867400.0,
        "currency": "$",
        "unit": "Per Wind turbine ("
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "CNG Bus",
        "cost": 3100000.0,
        "currency": "₹",
        "unit": "per bus (40 seater)"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "Hydrogen Powered Train",
        "cost": 800000000.0,
        "currency": "₹",
        "unit": "Cost of each hydrogen-powered train"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "Hydrogen Fuel Cell Bus",
        "cost": 10600000.0,
        "currency": "₹",
        "unit": "EKA 9H-Hydrogen Bus"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "2 Wh EV",
        "cost": 100000.0,
        "currency": "₹",
        "unit": "Per Vehicle"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "3 Wh EV- Passanger",
        "cost": 350000.0,
        "currency": "₹",
        "unit": "Per Vehicle"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "4 Wh EV- Passanger",
        "cost": 1500000.0,
        "currency": "₹",
        "unit": "Per Vehicle"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "E Bus- Passanger",
        "cost": 7000000.0,
        "currency": "₹",
        "unit": "Per Vehicle"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "3 Wh EV- Cargo",
        "cost": 300000.0,
        "currency": "₹",
        "unit": "Per Vehicle"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "EV MCV",
        "cost": 1100000.0,
        "currency": "₹",
        "unit": "Per Vehicle"
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "process": None,
        "action": "EV HCV",
        "cost": 1500000.0,
        "currency": "₹",
        "unit": "Per Vehicle"
    },
    {
        "sector": "Transport",
        "subsector": "Railway",
        "process": None,
        "action": "Metro",
        "cost": 750000000.0,
        "currency": "₹",
        "unit": "Per km (including train)"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Waste stabilisation pond system",
        "cost": 3000000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Duckweed Pond System",
        "cost": 3000000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Facultative Aerated lagoon",
        "cost": 2500000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Activated sludge process",
        "cost": 3000000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Biofor",
        "cost": 7500000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "High rate activated sludge Biofor F Technology",
        "cost": 5200000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Fluidized Aerated Bed (FAB)",
        "cost": 3500000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Submerged Aeration Fixed Film (SAFF) technology",
        "cost": 7000000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Wastewater",
        "subsector": "STP",
        "process": None,
        "action": "Up flow Anaerobic Sludge Blanket (UASB) process",
        "cost": 3000000.0,
        "currency": "₹",
        "unit": "Per MLD capacity"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "LED lights",
        "cost": 200.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "BLDC Fans",
        "cost": 1500.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "5 Star Rating Heater",
        "cost": 16000.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "3 Star Rating Heater",
        "cost": 10000.0,
        "currency": "₹",
        "unit": None
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "5 Star Rating AC",
        "cost": 50000.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "3 Star Rating AC",
        "cost": 25000.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "5 Star Rating Appliances",
        "cost": 1.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Residential",
        "process": "Super ECSBC",
        "action": "3 Star Rating Appliances",
        "cost": 1.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Comercial",
        "process": "Super ECSBC",
        "action": "LED lights",
        "cost": 2000.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Comercial",
        "process": "Super ECSBC",
        "action": "BLDC Fans",
        "cost": 3700.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Comercial",
        "process": "Super ECSBC",
        "action": "5 Star Rating Heater",
        "cost": 16000.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Comercial",
        "process": "Super ECSBC",
        "action": "5 Star Rating AC",
        "cost": 50000.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Comercial",
        "process": "Super ECSBC",
        "action": "5 Star Rating Appliances",
        "cost": 1.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Public and Institutional",
        "process": "Super ECSBC",
        "action": "LED lights",
        "cost": 2000.0,
        "currency": "₹",
        "unit": "Per Sqm"
    },
    {
        "sector": "Building and Energy",
        "subsector": "Public and Institutional",
        "process": "Super ECSBC",
        "action": "BLDC Fans",
        "cost": 3700.0,
        "currency": "₹",
        "unit": "Per Sqm"
    }
]

# ─── Strategies / actions from Stratergies & Cost sheet (r4-81) ─────────────
STRATEGIES = [
    {
        "sector": "Energy Sector",
        "subsector": "Residential",
        "strategy": "Super ECSBC",
        "action": "LED Lights",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": None
    },
    {
        "sector": "Energy Sector",
        "subsector": "Residential",
        "strategy": "Super ECSBC",
        "action": "5 star rating appliances",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 10.257
    },
    {
        "sector": "Energy Sector",
        "subsector": "Residential",
        "strategy": "Super ECSBC",
        "action": "5 star rating heater",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 0.0
    },
    {
        "sector": "Energy Sector",
        "subsector": "Residential",
        "strategy": "Super ECSBC",
        "action": "5 star rating AC",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 12.624
    },
    {
        "sector": "Energy Sector",
        "subsector": "Residential",
        "strategy": "Super ECSBC",
        "action": "BLDC fan",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 0.023670000000000073
    },
    {
        "sector": "Energy Sector",
        "subsector": "Commercial",
        "strategy": "Super ECSBC",
        "action": "LED Lights",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 0.014580000000000003
    },
    {
        "sector": "Energy Sector",
        "subsector": "Commercial",
        "strategy": "Super ECSBC",
        "action": "5 star rating appliances",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 0.03645
    },
    {
        "sector": "Energy Sector",
        "subsector": "Commercial",
        "strategy": "Super ECSBC",
        "action": "5 star rating heater",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 0.0
    },
    {
        "sector": "Energy Sector",
        "subsector": "Commercial",
        "strategy": "Super ECSBC",
        "action": "5 star rating AC",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 0.08262
    },
    {
        "sector": "Energy Sector",
        "subsector": "Commercial",
        "strategy": "Super ECSBC",
        "action": "BLDC fan",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": 0.004860000000000001
    },
    {
        "sector": "Energy Sector",
        "subsector": "Public & Institutional",
        "strategy": "Super ECSBC",
        "action": "LED Lights",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": None
    },
    {
        "sector": "Energy Sector",
        "subsector": "Public & Institutional",
        "strategy": "Super ECSBC",
        "action": "5 star rating appliances",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": None
    },
    {
        "sector": "Energy Sector",
        "subsector": "Public & Institutional",
        "strategy": "Super ECSBC",
        "action": "5 star rating heater",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": None
    },
    {
        "sector": "Energy Sector",
        "subsector": "Public & Institutional",
        "strategy": "Super ECSBC",
        "action": "5 star rating AC",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": None
    },
    {
        "sector": "Energy Sector",
        "subsector": "Public & Institutional - Streetlights",
        "strategy": "Super ECSBC",
        "action": "LED Lights",
        "bau_value": None,
        "unit": "MWh",
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Mode Shift",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Mode Shift",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Mode Shift",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Mode Shift",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "Railway",
        "strategy": "Mode Shift",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "Water Borne Navigation",
        "strategy": "Mode Shift",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "Aviation",
        "strategy": "Mode Shift",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Vehicle Fuel Switch",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Vehicle Fuel Switch",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Vehicle Fuel Switch",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "On Road",
        "strategy": "Vehicle Fuel Switch",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "Railway",
        "strategy": "Vehicle Fuel Switch",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "Water Borne Navigation",
        "strategy": "Vehicle Fuel Switch",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Transport",
        "subsector": "Aviation",
        "strategy": "Vehicle Fuel Switch",
        "action": None,
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Waste",
        "subsector": "Solid Waste Disposal",
        "strategy": None,
        "action": "Manage Landfill",
        "bau_value": 0.0,
        "unit": "Tonnes",
        "ep_value": None
    },
    {
        "sector": "Solid Waste",
        "subsector": "Organic Waste Treatment",
        "strategy": None,
        "action": "Composting",
        "bau_value": 0.0,
        "unit": "Tonnes",
        "ep_value": 0.0
    },
    {
        "sector": "Solid Waste",
        "subsector": "Organic Waste Treatment",
        "strategy": None,
        "action": "Anaerobic Process",
        "bau_value": 0.0,
        "unit": "Tonnes",
        "ep_value": None
    },
    {
        "sector": "Solid Waste",
        "subsector": "Dry Waste Treatment",
        "strategy": None,
        "action": "Incineration Process",
        "bau_value": 0.0,
        "unit": "Tonnes",
        "ep_value": None
    },
    {
        "sector": "Solid Waste",
        "subsector": "Dry Waste Treatment",
        "strategy": None,
        "action": "Open Burning Process",
        "bau_value": 0.0,
        "unit": "Tonnes",
        "ep_value": None
    },
    {
        "sector": "Solid Waste",
        "subsector": "Dry Waste Treatment",
        "strategy": None,
        "action": "Recycling",
        "bau_value": 0.0,
        "unit": "Tonnes",
        "ep_value": 0.0
    },
    {
        "sector": "Solid Waste",
        "subsector": "Waste Treatment",
        "strategy": None,
        "action": "Open Dumping",
        "bau_value": None,
        "unit": None,
        "ep_value": 0.0
    },
    {
        "sector": "Wastewater",
        "subsector": "Aerobic Treatment",
        "strategy": None,
        "action": "Centralised aerobic wastewater treatment plants (MBR/MMBR/SBR)",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Aerobic Treatment",
        "strategy": None,
        "action": "Aerobic shallow ponds",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Anaerobic Treatment",
        "strategy": None,
        "action": "Anaerobic lagoons",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Anaerobic Treatment",
        "strategy": None,
        "action": "Facultative lagoons",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Anaerobic Treatment",
        "strategy": None,
        "action": "Constructed wetlands",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Anaerobic Treatment",
        "strategy": None,
        "action": "Anaerobic reactors (MBR/MBBR/SBR)",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Onsite Sludge Management",
        "strategy": None,
        "action": "Sludge anaerobic treatment in centralised aerobic wastewater treatment plant (MBR/MBBR/SBR)",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Onsite Sludge Management",
        "strategy": None,
        "action": "Composting",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Onsite Sludge Management",
        "strategy": None,
        "action": "Incineration Process",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "Wastewater",
        "subsector": "Onsite Sludge Management",
        "strategy": None,
        "action": "Open Burning Process",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Live Stock",
        "strategy": None,
        "action": "Feeding Materials",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Live Stock",
        "strategy": None,
        "action": "Plant Bioactive Compound",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Manure Management",
        "strategy": None,
        "action": "Anaerobic Treatment",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Manure Management",
        "strategy": None,
        "action": "Composting",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Manure Management",
        "strategy": None,
        "action": "Community Biogas Plant",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Land Management",
        "strategy": None,
        "action": "Afforestation/Reforestation",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Land Management",
        "strategy": None,
        "action": "Soil Carbon Sequestration",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Land Management",
        "strategy": None,
        "action": "Wetland Restoration",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Land Management",
        "strategy": None,
        "action": "Improved Livestock Management",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Land Management",
        "strategy": None,
        "action": "Agroforestry",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "AFOLU",
        "subsector": "Land Management",
        "strategy": None,
        "action": "Biochar Application",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "Fly ash",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "Natural Pozzolanas",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "Calcined clay",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "Calcined clay with",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "Limestone",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "CSS—Direct separation",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "CCS—Advanced amines",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Cement Industry",
        "strategy": None,
        "action": "CCS—Molten carbonate fuel cell",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Lime Industry",
        "strategy": None,
        "action": "Chemical Synthesis",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Lime Industry",
        "strategy": None,
        "action": "Electro-Chemical Synthesis",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Lime Industry",
        "strategy": None,
        "action": "CCS—Partial Oxyfuel",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Lime Industry",
        "strategy": None,
        "action": "CSS—Direct separation",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Lime Industry",
        "strategy": None,
        "action": "CCS—Advanced amines",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    },
    {
        "sector": "IPPU",
        "subsector": "Lime Industry",
        "strategy": None,
        "action": "CCS—Molten carbonate fuel cell",
        "bau_value": None,
        "unit": None,
        "ep_value": None
    }
]


# ─── Helpers ────────────────────────────────────────────────────────────────
def actions_for_sector(sector):
    """Return all decarbonisation actions for a given sector (case-sensitive)."""
    return [a for a in DECARB_COSTS if a["sector"] == sector]

def cost_of_action(sector, action):
    """Look up the cost of a single decarbonisation action."""
    for a in DECARB_COSTS:
        if a["sector"] == sector and a["action"] == action:
            return a
    return None

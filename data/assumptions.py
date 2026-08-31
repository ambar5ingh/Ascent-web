"""
Calculation assumptions — climate-zone energy demand, waste/wastewater MCFs,
IPPU and AFOLU emission factors, and other defaults.
Mostly sourced from the "Assumption" sheet; IPCC tables noted in comments.
"""

# ─── Building energy demand (kWh/m²/yr) by climate zone ──────────────────────
# Source: Assumption sheet, rows 7-77; values match the existing app.py.
ENERGY_DEMAND = {'Hot and Dry': {'Residential': {'fan': 1, 'pump': 0, 'cool': 20, 'heat': 0, 'equip': 13, 'light': 7, 'total': 41}, 'Commercial': {'fan': 18, 'pump': 7, 'cool': 25, 'heat': 0, 'equip': 19, 'light': 8, 'total': 77}, 'Public/Inst': {'fan': 18, 'pump': 7, 'cool': 25, 'heat': 0, 'equip': 19, 'light': 8, 'total': 77}, 'Manufacturing': {'fan': 0, 'pump': 0, 'cool': 0, 'heat': 0, 'equip': 0, 'light': 0, 'total': 0}}, 'Warm and Humid': {'Residential': {'fan': 1, 'pump': 0, 'cool': 16, 'heat': 0, 'equip': 13, 'light': 7, 'total': 37}, 'Commercial': {'fan': 13, 'pump': 2, 'cool': 34, 'heat': 0, 'equip': 15, 'light': 6, 'total': 70}, 'Public/Inst': {'fan': 13, 'pump': 2, 'cool': 34, 'heat': 0, 'equip': 15, 'light': 6, 'total': 70}, 'Manufacturing': {'fan': 0, 'pump': 0, 'cool': 0, 'heat': 0, 'equip': 0, 'light': 0, 'total': 0}}, 'Composite': {'Residential': {'fan': 1, 'pump': 0, 'cool': 15, 'heat': 0, 'equip': 13, 'light': 7, 'total': 36}, 'Commercial': {'fan': 16, 'pump': 5, 'cool': 22, 'heat': 0, 'equip': 16, 'light': 7, 'total': 66}, 'Public/Inst': {'fan': 16, 'pump': 5, 'cool': 22, 'heat': 0, 'equip': 16, 'light': 7, 'total': 66}, 'Manufacturing': {'fan': 0, 'pump': 0, 'cool': 0, 'heat': 0, 'equip': 0, 'light': 0, 'total': 0}}, 'Temperate': {'Residential': {'fan': 0, 'pump': 0, 'cool': 8, 'heat': 0, 'equip': 13, 'light': 7, 'total': 28}, 'Commercial': {'fan': 17, 'pump': 5, 'cool': 18, 'heat': 0, 'equip': 18, 'light': 7, 'total': 65}, 'Public/Inst': {'fan': 17, 'pump': 5, 'cool': 18, 'heat': 0, 'equip': 18, 'light': 7, 'total': 65}, 'Manufacturing': {'fan': 0, 'pump': 0, 'cool': 0, 'heat': 0, 'equip': 0, 'light': 0, 'total': 0}}, 'Cold': {'Residential': {'fan': 0.8, 'pump': 0, 'cool': 6.1, 'heat': 12.3, 'equip': 13.4, 'light': 6.6, 'total': 39.2}, 'Commercial': {'fan': 15.2, 'pump': 4.5, 'cool': 9.6, 'heat': 17.6, 'equip': 12.7, 'light': 5.2, 'total': 64.8}, 'Public/Inst': {'fan': 15.2, 'pump': 4.5, 'cool': 9.6, 'heat': 17.6, 'equip': 12.7, 'light': 5.2, 'total': 64.8}, 'Manufacturing': {'fan': 0, 'pump': 0, 'cool': 0, 'heat': 0, 'equip': 0, 'light': 0, 'total': 0}}}

# ─── Solid Waste — landfill MCF by site type (Assumption sheet r83-91) ──────
SW_LANDFILL_MCF = {'Managed': 1.0, 'Managed well – semi-aerobic': 0.5, 'Managed poorly – semi-aerobic': 0.7, 'Managed well – active aeration': 0.4, 'Managed poorly – active aeration': 0.7, 'Unmanaged (≥5 m deep)': 0.8, 'Unmanaged (< 5m deep)': 0.4, 'Uncategorized': 0.6}

# ─── Solid Waste — DOC fractions (IPCC 2006 Table 2.4) ──────────────────────
SW_DOC = {'food': 0.15, 'garden': 0.2, 'paper': 0.4, 'wood': 0.43, 'textile': 0.24, 'rubber': 0.39}

# ─── Solid Waste — other fractions (Assumption r94, r95) ────────────────────
SW_FRACTIONS = {'fraction_ch4_in_landfill_gas': 0.5, 'fraction_doc_degraded': 0.6}

# ─── Solid Waste — incineration CH4 EFs (Assumption r99-104) ────────────────
# Key: (incineration_type, technology) → kg CH4 / Gg waste
SW_INCINERATION_CH4 = {
    ('Continuous incineration', 'Stoker'): 0.2,
    ('Continuous incineration', 'Fluidised bed'): 0.0,
    ('Semi-continuous incineration', 'Stoker'): 6.0,
    ('Semi-continuous incineration', 'Fluidised bed'): 188.0,
    ('Batch type incineration', 'Stoker'): 60.0,
    ('Batch type incineration', 'Fluidised bed'): 237.0,
}

# ─── Wastewater MCFs (IPCC 2006 Table 6.3) ──────────────────────────────────
WW_MCF = {'aerobic_centralised': 0.0, 'aerobic_ponds': 0.0, 'anaerobic_lagoon': 0.8, 'facultative_lagoon': 0.2, 'constructed_wetland': 0.0, 'anaerobic_reactor': 0.8, 'sludge_anaerobic': 0.8, 'composting': 0.0, 'septic': 0.5, 'open_pit': 0.1, 'open_discharge': 0.06}

# ─── IPPU emission factors (IPCC 2019) ──────────────────────────────────────
IPPU_EF = {'cement_clinker': 0.51, 'lime_high_ca': 0.785, 'lime_dolomite': 0.913, 'limestone': 0.48, 'dolomite': 0.48, 'steel_bof': 1.8, 'steel_eaf': 0.1, 'ammonia': 1.694, 'hno3_n2o': 9.0, 'glass_ef': 0.2}

# ─── AFOLU enteric fermentation EFs (kg CH4 / head / yr) ────────────────────
AFOLU_ENTERIC = {'dairy_cow_indigenous': 28, 'nondairy_cow_adult': 32, 'dairy_cow_crossbred': 43, 'dairy_buffalo': 50, 'sheep': 5, 'goat': 5, 'camel': 46, 'horse': 18, 'swine': 1, 'poultry': 0}

# ─── AFOLU manure management CH4 EFs (kg CH4 / head / yr) ───────────────────
AFOLU_MANURE_CH4 = {'dairy_cow_indigenous': 3.5, 'nondairy_cow_adult': 2.9, 'dairy_cow_crossbred': 3.8, 'dairy_buffalo': 4.4, 'sheep': 0.2, 'goat': 0.22, 'camel': 2.56, 'horse': 2.19, 'swine': 4.0, 'poultry': 0.02}

# ─── Transportation fuel energy contents (Assumption r123-129) ──────────────
# Used by the questionnaire-style transport calculator.
TRANSPORT_FUEL_ENERGY = {'Petrol': {'energy_mj': 32.0, 'value_tj': 0.032, 'unit': 'TJ/kL'}, 'Diesel': {'energy_mj': 35.7, 'value_tj': 0.0357, 'unit': 'TJ/kL'}, 'LPG': {'energy_mj': 24.4, 'value_tj': 0.0244, 'unit': 'TJ/t'}, 'CNG': {'energy_mj': 35.2, 'value_tj': 0.0352, 'unit': 'TJ/t'}, 'PNG': {'energy_mj': 20.4, 'value_tj': 0.0204, 'unit': 'TJ/t'}, 'Aviation Gasoline': {'energy_mj': 20.4, 'value_tj': 0.0204, 'unit': 'TJ/t'}}

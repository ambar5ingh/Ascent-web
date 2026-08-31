"""
GWP (Global Warming Potential) values — IPCC AR6.
Source: GWP sheet of WRI_India___ASCENT_Beta_V9.xlsm
"""

# AR6 100-year GWP values
GWP_CH4 = 29.8
GWP_N2O = 273.0

# Convenience map
GWP = {
    "CH4": GWP_CH4,
    "N2O": GWP_N2O,
    "CO2": 1.0,
}

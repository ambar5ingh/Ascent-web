"""
ASCENT — data package
=====================

All calculation constants extracted from WRI_India___ASCENT_Beta_V9.xlsm
(56 sheets) live under this package. app.py only imports what it needs.

Modules
-------
    gwp                — AR6 GWP values (CH4 = 29.8, N2O = 273)
    emission_factors   — Per-sector fuel EFs + ethanol blends
                         (also exports legacy flat EF[...] dict)
    assumptions        — Climate-zone energy demand, waste / wastewater MCFs,
                         IPPU and AFOLU defaults
    strategies         — Decarbonisation actions, sector abatement costs,
                         FX rates, fuel cost-per-kWh table
    conv_factors       — Fuel → TJ conversion + generic per-fuel EFs
                         (used by the questionnaire-driven calculator)
    unit_conversions   — Volume, mass, SI-prefix tables
    cities             — 4,900+ India city master with climate zone

Convenience: this __init__ re-exports the most commonly used names so
`from data import EF, GWP_CH4, INDIA_CITIES` works alongside the per-module
imports.
"""

from .gwp                import GWP_CH4, GWP_N2O, GWP
from .emission_factors   import (
    EF, EF_BY_SECTOR, ETHANOL_BLENDS, LEGACY_EF_MAP, get_ef,
)
from .assumptions        import (
    ENERGY_DEMAND, SW_LANDFILL_MCF, SW_DOC, SW_FRACTIONS,
    SW_INCINERATION_CH4, WW_MCF, IPPU_EF,
    AFOLU_ENTERIC, AFOLU_MANURE_CH4, TRANSPORT_FUEL_ENERGY,
)
from .strategies         import (
    ABATEMENT_COST, FX_RATES, FUEL_COSTS, DECARB_COSTS, STRATEGIES,
    actions_for_sector, cost_of_action,
)
from .conv_factors       import (
    CONV_FACTORS, GENERIC_FUEL_EF, tj_factor, emit_for_fuel,
)
from .unit_conversions   import (
    VOLUME_FROM_TO, MASS_FROM_TO, SI_PREFIX, FUEL_CONV,
    convert_volume, convert_mass,
)
from .cities             import (
    INDIA_CITIES, STATES,
    cities_for_state, cities_for_district, lookup_city,
)

__all__ = [
    # gwp
    "GWP_CH4", "GWP_N2O", "GWP",
    # emission factors
    "EF", "EF_BY_SECTOR", "ETHANOL_BLENDS", "LEGACY_EF_MAP", "get_ef",
    # assumptions
    "ENERGY_DEMAND", "SW_LANDFILL_MCF", "SW_DOC", "SW_FRACTIONS",
    "SW_INCINERATION_CH4", "WW_MCF", "IPPU_EF",
    "AFOLU_ENTERIC", "AFOLU_MANURE_CH4", "TRANSPORT_FUEL_ENERGY",
    # strategies
    "ABATEMENT_COST", "FX_RATES", "FUEL_COSTS", "DECARB_COSTS", "STRATEGIES",
    "actions_for_sector", "cost_of_action",
    # conv factors
    "CONV_FACTORS", "GENERIC_FUEL_EF", "tj_factor", "emit_for_fuel",
    # units
    "VOLUME_FROM_TO", "MASS_FROM_TO", "SI_PREFIX", "FUEL_CONV",
    "convert_volume", "convert_mass",
    # cities
    "INDIA_CITIES", "STATES",
    "cities_for_state", "cities_for_district", "lookup_city",
]

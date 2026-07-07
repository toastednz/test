"""Configuration: Stats NZ source URLs, series mappings, and weight regimes.

Series reference conventions (Stats NZ Infoshare):
  CPIQ.SE<code>  quarterly CPI index numbers (the official measure)
  CPIM.SE<code>  monthly selected price indexes (SPI) / food price index (FPI)

The monthly and quarterly class codes coincide (e.g. SE901102 = Vegetables),
which is what makes a clean bottom-up mapping possible.
"""

STATS_NZ_BASE = "https://www.stats.govt.nz"

# Static reference: CPI review 2024 tables (expenditure weights by group,
# subgroup, and class for the Sep-2017, Jun-2020, and Dec-2024 base quarters).
WEIGHTS_TABLES_URL = (
    STATS_NZ_BASE
    + "/assets/Methods/Consumers-price-indexes-review-2024/"
    + "consumers-price-index-review-2024-tables.xlsx"
)

# Release-asset URL templates. {Month}/{month} like "May"/"may", {year} like "2026".
SPI_CSV_TEMPLATE = (
    STATS_NZ_BASE
    + "/assets/Uploads/Selected-price-indexes/Selected-price-indexes-{Month}-{year}/"
    + "Download-data/selected-price-indexes-{month}-{year}.csv"
)
CPI_CSV_TEMPLATE = (
    STATS_NZ_BASE
    + "/assets/Uploads/Consumers-price-index/Consumers-price-index-{Month}-{year}-quarter/"
    + "Download-data/consumers-price-index-{month}-{year}-quarter-index-numbers.csv"
)

MONTH_NAMES = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
]

# Quarterly CPI headline series.
ALL_GROUPS = "CPIQ.SE9A"

# Monthly SPI series mapped onto the quarterly CPI class they price.
# These are the components of the CPI basket with a public monthly source.
SPI_TO_CLASS = {
    # Food price index, level-3 classes (monthly since 1960 at group level)
    "CPIM.SE901101": "CPIQ.SE901101",  # Fruit
    "CPIM.SE901102": "CPIQ.SE901102",  # Vegetables
    "CPIM.SE901201": "CPIQ.SE901201",  # Meat and poultry
    "CPIM.SE901202": "CPIQ.SE901202",  # Fish and other seafood
    "CPIM.SE901301": "CPIQ.SE901301",  # Bread and cereals
    "CPIM.SE901302": "CPIQ.SE901302",  # Milk, cheese and eggs
    "CPIM.SE901303": "CPIQ.SE901303",  # Oils and fats
    "CPIM.SE901304": "CPIQ.SE901304",  # Food additives and condiments
    "CPIM.SE901305": "CPIQ.SE901305",  # Confectionery, nuts and snacks
    "CPIM.SE901306": "CPIQ.SE901306",  # Other grocery food
    "CPIM.SE901401": "CPIQ.SE901401",  # Coffee, tea and other hot drinks
    "CPIM.SE901402": "CPIQ.SE901402",  # Soft drinks, waters and juices
    "CPIM.SE901501": "CPIQ.SE901501",  # Restaurant meals
    "CPIM.SE901502": "CPIQ.SE901502",  # Ready-to-eat food
    # Alcoholic beverages and tobacco (monthly since Jun 2011)
    "CPIM.SE902101": "CPIQ.SE902101",  # Beer
    "CPIM.SE902102": "CPIQ.SE902102",  # Wine
    "CPIM.SE902103": "CPIQ.SE902103",  # Spirits and liqueurs
    "CPIM.SE902200": "CPIQ.SE902200",  # Cigarettes and tobacco
    # Household energy (monthly since Jun 2011)
    "CPIM.SE904501": "CPIQ.SE904501",  # Electricity
    "CPIM.SE904502": "CPIQ.SE904502",  # Gas
    # Rents: CPI uses the stock measure of the rental price index
    "CPIM.SE9041S": "CPIQ.SE904101",   # Actual rentals for housing (stock)
    # Vehicle fuels (monthly since Jun 2011)
    "CPIM.SE9072020000": "CPIQ.SE907202",  # Petrol (level-6 item -> Petrol class)
    "CPIM.SE9072030001": "CPIQ.SE907203",  # Diesel -> Other vehicle fuels and lubricants
    # Air transport (monthly since Jun 2015)
    "CPIM.SE907303": "CPIQ.SE907303",  # Domestic air transport
    "CPIM.SE907304": "CPIQ.SE907304",  # International air transport
    # Accommodation services (monthly since Jun 2017)
    "CPIM.SE909601": "CPIQ.SE909601",  # Domestic accommodation services
    "CPIM.SE909602": "CPIQ.SE909602",  # Overseas accommodation prepaid in NZ
}
CLASS_TO_SPI = {v: k for k, v in SPI_TO_CLASS.items()}

# Weight-table row labels that don't string-match the Infoshare class titles.
WEIGHT_NAME_ALIASES = {
    "purchase of new housing": "CPIQ.SE904201",
    "pet-related products": "CPIQ.SE909304",
    "overseas accommodation costs prepaid in new zealand": "CPIQ.SE909602",
    "tertiary and other post-school education": "CPIQ.SE910300",
    "other education": "CPIQ.SE910400",
    "credit services": "CPIQ.SE911501",
}

# Weight regimes: (weight column, base/link quarter, first quarterly movement
# calculated on these weights). The CPI is a chained Laspeyres-type index;
# within a regime the movement from the link quarter is a fixed-basket
# weighted average of class movements.
#   2017 review -> introduced with the Dec-2017 quarter (link Sep 2017)
#   2020 review -> introduced with the Sep-2020 quarter (link Jun 2020)
#   2024 review -> introduced with the Mar-2025 quarter (link Dec 2024)
WEIGHT_REGIMES = [
    ("w2024", "2024.12", "2025.03"),
    ("w2020", "2020.06", "2020.09"),
    ("w2017", "2017.09", "2017.12"),
]

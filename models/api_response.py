from dataclasses import dataclass
from typing import List

class AvailabilityStatus():
    IN_STOCK = "In Stock"
    LOW_STOCK = "Low Stock"


class Category():
    BEAUTY = "beauty"
    FRAGRANCES = "fragrances"
    FURNITURE = "furniture"
    GROCERIES = "groceries"


class ReturnPolicy():
    NO_RETURN_POLICY = "No return policy"
    THE_30_DAYS_RETURN_POLICY = "30 days return policy"
    THE_60_DAYS_RETURN_POLICY = "60 days return policy"
    THE_7_DAYS_RETURN_POLICY = "7 days return policy"
    THE_90_DAYS_RETURN_POLICY = "90 days return policy"


@dataclass
class APIResponse:
    products: List[Product]
    total: int
    skip: int
    limit: int
from dataclasses import dataclass
from typing import List
from models.product import Product

@dataclass
class APIResponse:
    products: List[Product]
    total: int
    skip: int
    limit: int
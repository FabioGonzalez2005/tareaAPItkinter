from dataclasses import dataclass
from datetime import datetime


@dataclass
class Meta:
    created_at: datetime
    updated_at: datetime
    barcode: str
    qr_code: str
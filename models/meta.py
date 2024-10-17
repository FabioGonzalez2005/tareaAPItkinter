from dataclasses import dataclass

@dataclass
class Meta:
    created_at: datetime
    updated_at: datetime
    barcode: str
    qr_code: str
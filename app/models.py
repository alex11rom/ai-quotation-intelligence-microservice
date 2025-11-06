from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Client(BaseModel):
    name: str
    contact: EmailStr
    lang: Optional[str] = "en"

class Item(BaseModel):
    sku: str
    qty: int
    unit_cost: float
    margin_pct: float

class QuoteRequest(BaseModel):
    client: Client
    currency: str
    items: List[Item]
    delivery_terms: str
    notes: Optional[str] = ""

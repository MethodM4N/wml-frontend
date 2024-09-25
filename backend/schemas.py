from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

from backend.database import str_50, str_255, num_9_2


class SProductAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str_50 = Field(min_length=1, max_length=50)
    price: Optional[num_9_2] = Field(None, max_digits=9, decimal_places=2)
    model: Optional[str_255] = Field(None, max_length=255)
    is_purchased: bool = False
    buy_date: Optional[datetime] = None
    guarantee: int = 0
    receipt: Optional[str] = None
    shop: Optional[str_255] = Field(None, max_length=255)
    priority: Optional[int] = None


class SProduct(SProductAdd):
    id: int
    guarantee_end_date: Optional[datetime] = None


class SResolve(BaseModel):
    ok: bool = True
    product_id: int
    message: Optional[str] = None

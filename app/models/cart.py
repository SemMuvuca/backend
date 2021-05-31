from typing import List
from pydantic import BaseModel


class products(BaseModel):
    ean13_code: str
    quantity: int


class checkout_list(BaseModel):
    products_quantity: List[products]

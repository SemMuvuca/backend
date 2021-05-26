from typing import List
from pydantic import BaseModel


class Atributes(BaseModel):
    ean13_code: str
    quantity: int


class Codes(BaseModel):
    atributes_list: List[Atributes]

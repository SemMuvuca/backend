from pydantic import BaseModel


class Item(BaseModel):
    id: int
    color: str
    mass: float


class CreateItem(BaseModel):
    color: str
    mass: float


# Allowing the user to only update the color
class UpdateItem(BaseModel):
    color: str

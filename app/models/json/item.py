from tortoise.contrib.pydantic import pydantic_model_creator
from models.database.itemSchema import Item

ItemSchema = pydantic_model_creator(
    Item, name=f"{Item.__name__}Schema", sort_alphabetically=True
)
ItemSchemaCreate = pydantic_model_creator(
    Item,
    name=f"{Item.__name__}SchemaCreate",
    sort_alphabetically=True,
    exclude_readonly=False,
)

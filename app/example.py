from fastapi import FastAPI
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields, Tortoise

TORTOISE_ORM = {
    "connections": {"default": "sqlite://./test.db"},
    "apps": {
        "models": {
            "models": ["example"],
            "default_connection": "default",
        },
    },
}

# Create Database Tables
async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


app = FastAPI()
register_tortoise(app, config=TORTOISE_ORM)


# Tortoise ORM Model
class Item(Model):
    product_name = fields.IntField(null=False, description=f"Name of the product")
    quantity = fields.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2,
        description=f"Volume or weight value",
    )
    code = fields.TextField(null=False, description=f"EAN13 code")
    created_at = fields.DatetimeField(
        null=False,
        auto_now_add=True,
        editable=False,
        description=f"Day when the item was inserted on the database",
    )
    modified_at = fields.DatetimeField(
        null=False,
        auto_now=True,
        editable=True,
        description=f"Day when the item was inserted on the database",
    )


# Pydantic schema
TestSchema = pydantic_model_creator(Item, name=f"{Item.__name__}Schema")
TestSchemaCreate = pydantic_model_creator(
    Item, name=f"{Item.__name__}SchemaCreate", exclude_readonly=True
)

# Make your FastAPI Router from your Pydantic schema and Tortoise Model
router = TortoiseCRUDRouter(
    schema=TestSchema,
    create_schema=TestSchemaCreate,
    db_model=Item,
    prefix=Item.__name__,
    delete_all_route=False,
    get_all_route=False,
)

# Add it to your app
app.include_router(router)

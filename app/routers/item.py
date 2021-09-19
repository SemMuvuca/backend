from models.json.item import ItemSchema, ItemSchemaCreate
from models.database.itemSchema import Item
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter


# Make your FastAPI Router from your Pydantic schema and Tortoise Model
router = TortoiseCRUDRouter(
    schema=ItemSchema,
    create_schema=ItemSchemaCreate,
    db_model=Item,
    prefix=Item.__name__,
    delete_all_route=False,
    get_all_route=False,
)

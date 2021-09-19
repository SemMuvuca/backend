from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from routers import item


TORTOISE_ORM = {
    "connections": {"default": "sqlite://./test.db"},
    "apps": {
        "models": {
            "models": ["models.database.itemSchema"],
            "default_connection": "default",
        },
    },
}


# Create Database Tables
async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
register_tortoise(app, config=TORTOISE_ORM)


# Add it to your app
app.include_router(item.router)

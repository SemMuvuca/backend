import httpx
import os
from datastore import client as db_client
from queries import simple_query

base_url: str = (
    f"https://api.mercadopago.com/instore/qr/seller/collectors/{os.getenv('USER_ID')}"
)
create_order_url: str = f"{base_url}/stores/{os.getenv('EXTERNAL_STORE_ID')}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"
get_order_url: str = f"{base_url}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"

headers = {"Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}"}

async def create_order():
    order = {
    "external_reference": 12345,
    "title": "Product order",
    "description": "This is the order",
    "notification_url": "www.yourserver.com",
    "total_amount": 100
    "items": [
        # {
        # "sku_number": "A123K9191938",
        # "category": "marketplace",
        # "title": "Point Mini",
        # "description": "This is the Point Mini",
        # "unit_price": 100,
        # "quantity": 1,
        # "unit_measure": "unit",
        # "total_amount": 100
        # }
    ]
    }
    with httpx.Client(headers=headers) as client:
        return client.put(create_order_url)


async def status_order():
    with httpx.Client(headers=headers) as client:
        return client.get(create_order_url)

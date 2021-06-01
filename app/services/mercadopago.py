import os

from fastapi.encoders import jsonable_encoder
import httpx

from database.datastore import get_product

base_url: str = (
    f"https://api.mercadopago.com/instore/qr/seller/collectors/{os.getenv('USER_ID')}"
)
create_order_url: str = f"{base_url}/stores/{os.getenv('EXTERNAL_STORE_ID')}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"
get_order_url: str = f"{base_url}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"
headers = {"Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"}


async def create_order(products):
    product_list = []
    total_amount = 0.0
    for item in products["products_quantity"]:
        produto = await get_product(item["ean13_code"])
        product_list.append(
            {
                "title": produto["title"],
                "description": produto["description"],
                "category": produto["category"],
                "unit_measure": produto["unit_measure"],
                "unit_price": produto["unit_price"],
                "quantity": item["quantity"],
                "total_amount": produto["unit_price"] * item["quantity"],
            }
        )
        total_amount += produto["unit_price"] * item["quantity"]
    order = {
        "external_reference": 12345,
        "title": "Product order",
        "description": "This is the order",
        "notification_url": "https://hookb.in/pza3ZNO01DuXNNqwBgyk",
        "total_amount": total_amount,
        "items": product_list,
    }
    with httpx.Client(headers=headers) as client:
        return client.put(url=create_order_url, data=jsonable_encoder(order))


async def get_status_order():
    with httpx.Client(headers=headers) as client:
        return client.get(create_order_url)

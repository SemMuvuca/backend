# import os
# import requests
import httpx
from database.datastore import get_product
from fastapi.encoders import jsonable_encoder

# base_url: str = (
#     f"https://api.mercadopago.com/instore/qr/seller/collectors/{os.getenv('USER_ID')}"
# )
# create_order_url: str = f"{base_url}/stores/{os.getenv('EXTERNAL_STORE_ID')}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"
# get_order_url: str = f"{base_url}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"

async def create_order(products):
    product_list = []
    total_amount = 0.0
    for item in products["products_quantity"]:
        produto = get_product(item["ean13_code"])
        product_list.append(
            {
                "category": produto["category"],
                "title": produto["title"],
                "description": produto["description"],
                "unit_price": produto["unit_price"],
                "quantity": item["quantity"],
                "unit_measure": produto["unit_measure"],
                "total_amount": produto["unit_price"] * item["quantity"],
            }
        )
        total_amount += produto["unit_price"] * item["quantity"]
    order = {
        "external_reference": "12345",
        "title": "Product order",
        "description": "quenga",
        "notification_url": "sem-muvuca.rj.r.appspot.com/mercadopago/ipn",
        "total_amount": total_amount,
        "items": product_list,
    }
    # headers = {
    #     "Authorization": "APP_USR-2350858020961763-060102-0a86961866fa461c4a9aae7326871d92-235427759"
    # }
    with httpx.Client() as client:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer APP_USR-2350858020961763-060102-0a86961866fa461c4a9aae7326871d92-235427759"
        }

        print(headers)
        # print(create_order_url)
        print(order)

        r = client.put(
            url="https://api.mercadopago.com/instore/qr/seller/collectors/235427759/stores/LOJA1337/pos/CAIXA8080/orders",
            data=jsonable_encoder(order),
            headers=headers,
        )

        print(r.request.headers)
        print(r.json)
    
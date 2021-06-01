import os

from fastapi.encoders import jsonable_encoder
import httpx

from database.datastore import get_product

base_url: str = (
    f"https://api.mercadopago.com/instore/qr/seller/collectors/{os.getenv('USER_ID')}"
)
create_order_url: str = f"{base_url}/stores/{os.getenv('EXTERNAL_STORE_ID')}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"
get_order_url: str = f"{base_url}/pos/{os.getenv('EXTERNAL_POS_ID')}/orders"


async def create_order(products):
    product_list = []
    total_amount = 0.0
    for item in products["products_quantity"]:
        produto = get_product(item["ean13_code"])
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
        "external_reference": "12345",
        "title": "Product order",
        "description": "This is the order",
        "notification_url": "sem-muvuca.rj.r.appspot.com/mercadopago/ipn",
        "total_amount": total_amount,
        "items": product_list,
    }
    headers = {
        "Authorization": "Bearer APP_USR-1005181805798098-032819-0d61694407b2dc0f38266e2dfa533aab-235427759"
    }
    with httpx.Client(headers=headers) as client:
        headers = {"Content-Type": "application/json"}
        print(headers)
        print(create_order_url)
        print(jsonable_encoder(order))
        r = client.put(
            url="https://api.mercadopago.com/instore/qr/seller/collectors/235427759/stores/LOJA1337/pos/CAIXA8080/orders",
            data=jsonable_encoder(order),
            headers=headers,
        )
        print(r.request.headers)
        print(r)


async def get_status_order():
    headers = {
        "Authorization": "Bearer APP_USR-1005181805798098-032819-0d61694407b2dc0f38266e2dfa533aab-235427759"
    }
    with httpx.Client(headers=headers) as client:
        return client.get(create_order_url)

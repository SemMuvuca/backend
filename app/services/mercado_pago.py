import httpx
from database.datastore import get_product


async def create_order(products):
    product_list = []
    total_amount: float = 0.0
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
    print(order)
    with httpx.Client() as client:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer APP_USR-2350858020961763-060102-0a86961866fa461c4a9aae7326871d92-235427759",
        }
        r = client.put(
            url="https://api.mercadopago.com/instore/qr/seller/collectors/235427759/stores/LOJA1337/pos/CAIXA8080/orders",
            json=order,
            headers=headers,
        )
        print(r.request.headers)
        print(r)
        print(r.text)


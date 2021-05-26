import httpx

USER_ID: str = "None"
EXTERNAL_STORE_ID: str = "None"
EXTERNAL_POS_ID: str = "None"
base_url: str = f"https://api.mercadopago.com/instore/qr/seller/collectors/{USER_ID}"
create_order_url: str = (
    f"{base_url}/stores/{EXTERNAL_STORE_ID}/pos/{EXTERNAL_POS_ID}/orders"
)
get_order_url: str = f"{base_url}/pos/{EXTERNAL_POS_ID}/orders"
ACCESS_TOKEN = "None"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


async def create_order():
    with httpx.Client(headers=headers) as client:
        return client.put(create_order_url)


async def status_order():
    with httpx.Client(headers=headers) as client:
        return client.get(create_order_url)

from fastapi import APIRouter, status
import httpx

from services.mercado_pago import create_order

router = APIRouter(
    prefix="/mercadopago",
    tags=["Mercado Pago"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# @router.post("/ipn", status_code=status.HTTP_201_CREATED)
# async def notification(topic: str, id: int):
#     print(f"Notifying {topic} on {id}")


# @router.put("/create_order")
# async def new_order(checkout_list: checkout_list):
#     await create_order(jsonable_encoder(checkout_list))


@router.delete("/delete_order")
async def delete_order():
    with httpx.Client() as client:
        headers = {
            "Authorization": "Bearer APP_USR-2350858020961763-060102-0a86961866fa461c4a9aae7326871d92-235427759",
        }
        client.delete(
            url="https://api.mercadopago.com/instore/qr/seller/collectors/235427759/pos/CAIXA8080/orders",
            headers=headers,
        )

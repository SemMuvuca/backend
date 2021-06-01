from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from models.cart import checkout_list
from services.mercadopago import create_order

router = APIRouter(
    prefix="/mercadopago",
    tags=["Mercado Pago"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/ipn", status_code=status.HTTP_201_CREATED)
async def notification(topic: str, id: int):
    print(f"Notifying {topic} on {id}")


@router.put("/create_order")
async def new_order(checkout_list: checkout_list):
    await create_order(jsonable_encoder(checkout_list))

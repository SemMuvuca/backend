from fastapi import APIRouter, status

from models.mercado_pago import client_payment_data
from services.mercado_pago import status_order

router = APIRouter(
    prefix="/mercadopago",
    tags=["Mercado Pago"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/ipn", status_code=status.HTTP_201_CREATED)
async def notification(topic: str, id: int):
    print(f"Notifying {topic} on {id}")


@router.post("/process_payment", status_code=status.HTTP_201_CREATED)
async def payment(data: client_payment_data):
    return await status_order(data.__dict__)

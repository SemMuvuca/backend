from fastapi import APIRouter, status

router = APIRouter(
    prefix="/mercadopago",
    tags=["Mercado Pago"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/ipn", status_code=status.HTTP_201_CREATED)
async def notification(topic: str, id: int):
    print(f"Notifying {topic} on {id}")

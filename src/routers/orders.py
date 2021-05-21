from fastapi import APIRouter

import mercadopago
from mercadopago.config import RequestOptions

router = APIRouter(
    prefix="/order",
    tags=["Order"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/add/{code}")
async def scan_store(code: int):
    return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]

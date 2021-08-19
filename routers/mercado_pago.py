from fastapi import APIRouter, status
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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


@router.get("/payment/{total_amount}", response_class=HTMLResponse)
async def payment_page(request: Request, total_amount: int):
    return Jinja2Templates(directory="templates").TemplateResponse(
        "index.html", {"request": request, "total_amount": total_amount}
    )


@router.get("/payment/js/{total_amount}", response_class=HTMLResponse)
async def payment_js(request: Request, total_amount: int):
    return Jinja2Templates(directory="templates/js").TemplateResponse(
        "index.js", {"request": request, "total_amount": total_amount}
    )

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from database.firestore import get_product
from models.cart import checkout_list

router = APIRouter(
    prefix="/totem",
    tags=["Totem"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/query_cart")
async def product_query(checkout_list: checkout_list):
    order_list = jsonable_encoder(checkout_list)
    product_obj = {"total_price": 0.0, "total_weight": 0.0}
    for item in order_list["products_quantity"]:
        product_data = get_product(item["ean13_code"])
        product_obj["total_price"] += product_data["unit_price"] * item["quantity"]
        product_obj["total_weight"] += product_data["weight"] * item["quantity"]
    return jsonable_encoder(product_obj)

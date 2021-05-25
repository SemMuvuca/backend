from fastapi import APIRouter
from models.totem import Codes
from helpers.helper_queries import simple_query
from datastore import client as db_client
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/totem",
    tags=["Totem"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/query/")
async def product_query(codes: Codes) -> object:
    product_obj = {"total_price": 0.0, "total_weight": 0.0}
    products = codes.dict()
    for item in products["atributes_list"]:
        produto = await simple_query(
            db_client, "Produto", "barcode", "=", item["ean13_code"]
        )

        product_obj["total_price"] += produto["unit_price"] * item["quantity"]
        product_obj["total_weight"] += produto["weight"] * item["quantity"]

    return jsonable_encoder(product_obj)

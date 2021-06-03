from fastapi import APIRouter
from database.datastore import get_product
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    prefix="/scan",
    tags=["Scan"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/store/{ean_13}")
async def scan_store(ean_13: str):
    return jsonable_encoder(get_product(ean_13))


# @router.get("/openfood/{code}")
# async def scan_openfood(code: int):
#     return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]


# @router.get("/monster/{code}")
# async def scan_monster(code: int):
#     return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]

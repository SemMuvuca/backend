from fastapi import APIRouter, Response, status
from database.firestore import get_product

router = APIRouter(
    prefix="/scan",
    tags=["Scan"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/{ean_13}", status_code=status.HTTP_200_OK)
async def scan_store(ean_13: int, response: Response):
    requested_product = get_product(ean_13)
    if requested_product is None:
        response.status_code = status.HTTP_404_NOT_FOUND
    return requested_product


# @router.get("/openfood/{code}")
# async def scan_openfood(code: int):
#     return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]

# @router.get("/monster/{code}")
# async def scan_monster(code: int):
#     return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]

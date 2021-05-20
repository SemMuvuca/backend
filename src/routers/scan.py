from fastapi import APIRouter

router = APIRouter(
    prefix="/scan",
    tags=["Scan"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/store/{code}")
async def scan_store(code: int):
    return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]


@router.get("/openfood/{code}")
async def scan_openfood(code: int):
    return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]


@router.get("/monster/{code}")
async def scan_monster(code: int):
    return [{"Product": "Rick", "Brand": "Morty", "Price": 1, "Weight": 10}]

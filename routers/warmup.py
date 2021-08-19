from fastapi import APIRouter, status

router = APIRouter(prefix="/_ah", tags=["Warmup"])


@router.get("/warmup", status_code=status.HTTP_200_OK)
async def server_warmup():
    print("esquentando")

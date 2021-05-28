from fastapi import FastAPI

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
from routers import scan, mercado_pago, totem

app = FastAPI()
app.include_router(scan.router)
app.include_router(mercado_pago.router)
app.include_router(totem.router)

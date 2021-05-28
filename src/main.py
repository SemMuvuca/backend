from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
from routers import scan, mercado_pago, totem

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(scan.router)
app.include_router(mercado_pago.router)
app.include_router(totem.router)

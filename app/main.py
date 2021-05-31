from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import scan, mercado_pago, totem, warmup

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(warmup.router)
app.include_router(scan.router)
app.include_router(totem.router)
app.include_router(mercado_pago.router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from routers import scan, mercado_pago, totem, warmup
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Sem Muvuca",
    description="Python/FastAPI based service for all 'Sem Muvuca' functionality.",
    default_response_class=ORJSONResponse,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(warmup.router)
app.include_router(scan.router)
app.include_router(totem.router)
app.include_router(mercado_pago.router)
app.mount("/static/", StaticFiles(directory="static"), name="static")

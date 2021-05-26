from fastapi import FastAPI

# from .dependencies import get_query_token, get_token_header
# from .internal import admin
from routers import scan, mp, totem

app = FastAPI()
app.include_router(scan.router)
app.include_router(mp.router)
app.include_router(totem.router)

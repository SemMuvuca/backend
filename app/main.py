from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers, models
from fastapi.responses import ORJSONResponse
from tortoise.contrib.fastapi import register_tortoise
from routers import mercado_pago, warmup
from database.SQL import DATABASE_URL, user_db
from models.user import User, UserCreate, UserUpdate, UserDB
from services.JWT import jwt_authentication, SECRET
from dependencies import on_after_register, on_after_forgot_password

app = FastAPI(
    title="Sem Muvuca",
    description="Python/FastAPI based service for all 'Sem Muvuca' functionality.",
    default_response_class=ORJSONResponse,
)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app.include_router(warmup.router)

# register_tortoise(
#     app,
#     db_url=DATABASE_URL,
#     modules={"models": ["full_tortoise"]},
#     generate_schemas=True,
# )

# fastapi_users = FastAPIUsers(
#     user_db,
#     [jwt_authentication],
#     User,
#     UserCreate,
#     UserUpdate,
#     UserDB,
# )

# app.include_router(
#     fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
# )
# app.include_router(
#     fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
# )
# app.include_router(
#     fastapi_users.get_reset_password_router(
#         SECRET, after_forgot_password=on_after_forgot_password
#     ),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_verify_router(
#         SECRET, after_verification_request=after_verification_request
#     ),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])

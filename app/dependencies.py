from fastapi import Request
from models.user import UserDB


async def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


async def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


async def after_verification_request(user: UserDB, token: str, request: Request):
    print(f"Verification requested for user {user.id}. Verification token: {token}")

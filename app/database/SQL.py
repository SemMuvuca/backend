from fastapi_users.db import TortoiseUserDatabase
from models.user import UserDB, UserModel

DATABASE_URL = "sqlite://./test.db"

user_db = TortoiseUserDatabase(UserDB, UserModel)

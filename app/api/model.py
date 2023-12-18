from pydantic import BaseModel,EmailStr
from datetime import datetime


# performances = Table(
#     'users',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('email', String(50)),
#     Column('password', String(50)),
#     Column('username', String(20)),
#     Column('is_staff', Integer)
# )
class UserIn(BaseModel):
    email: str
    email: EmailStr
    password: str
    username: str
    username: str
    is_staff: int


class UserOut(UserIn):
    id: int


class UserUpdate(UserIn):
    email: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    username: str | None = None
    username: str | None = None
    is_staff: int | None = None

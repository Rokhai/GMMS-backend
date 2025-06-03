from pydantic import BaseModel
from typing import Optional
from enum import Enum

class SexEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class AccountStatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    suspended = "suspended"

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    # id: int = None
    first_name: str
    last_name: str
    sex: SexEnum
    email: str
    password: str
    is_subscribed: Optional[bool] = False

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    sex: Optional[SexEnum] = None
    account_status: Optional[AccountStatusEnum] = None
    role: Optional[RoleEnum] = None
    is_subscribed: Optional[bool] = None
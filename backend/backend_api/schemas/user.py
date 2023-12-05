from pydantic import BaseModel
from datetime import datetime

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    user_id: str
    username: str
    created_at: datetime

class Token(BaseModel):
    access_token: str

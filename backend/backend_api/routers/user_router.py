from fastapi import APIRouter, Depends, HTTPException
from backend.backend_api.schemas.user import UserIn, UserOut, Token
from backend.utils.databases import AsyncSQLDB
from sqlalchemy.ext.asyncio import AsyncSession
from backend.backend_api.services import user_service
import uuid
from backend.backend_api import security
from backend.backend_api.models import User
from datetime import datetime
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()
async_db = AsyncSQLDB()

@router.post("/register")
async def register_user(user_in: UserIn, db: AsyncSession = Depends(async_db.get_session)) -> UserOut:
    db_user = await user_service.get_user_by_username(db, user_in.username) 
    if db_user is not None:
        raise HTTPException(status_code=400, detail="Username already registered")
    else:
        hashed_password = security.get_hashed_password(user_in.password)
        user = User(user_id = str(uuid.uuid4()),
                    hashed_password = hashed_password,
                    **user_in.model_dump(exclude={"password"}),
                    )
        db_user = await user_service.add_user(db, user)

        return db_user

@router.post("/token")
async def create_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(async_db.get_session)) -> Token:
    db_user = await user_service.get_user_by_username(db, form_data.username) 
    if not security.pwd_context.verify(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    else:
        to_encode = {
            "sub": db_user.user_id,
            "username": form_data.username,
            "iat": datetime.utcnow(),
        }
        token = security.create_access_token(to_encode, security.TOKEN_EXPIRY_TIME) 

    return token

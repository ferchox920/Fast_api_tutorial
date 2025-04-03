from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import user_service
from app.schemas.user import UserCreate, UserOut
from typing import List

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db import get_db
from models import User
from schemas.user_schema import UserCreate, UserResponse,UserUpdateAPIKey

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()



@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user_update: UserUpdateAPIKey, db: Session = Depends(get_db)):
    user_repo=UserRepo(db)
    user=user_repo.update_user(user_id,user)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        user_api_key=user_update.api_key

    return user

@router.put("/users/{user_id}/api-key", response_model=UserResponse)
def update_user_api_key(user_id: str, user_update: UserUpdateAPIKey, db: Session = Depends(get_db)):
    user_repo=UserRepo(db)
    user=user_repo.update_user(user_id,user)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        user_api_key=user_update.api_key

    return user

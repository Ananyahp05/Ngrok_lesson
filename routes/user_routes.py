import logging
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from db import get_db
from models import User
from repositories.User_repo import UserRepo
from schemas.User_schemas import UserCreate, UserResponse

logger = logging.getLogger(__name__)
router = APIRouter()


# ─── Create User ──────────────────────────────────────────────────────────────

@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    user_repo = UserRepo(db)
    existing_user = user_repo.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    db_user = User(email=user.email, password=user.password)
    return user_repo.add_user(db_user)


# ─── Get All Users ────────────────────────────────────────────────────────────

@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    """Return a list of all users."""
    user_repo = UserRepo(db)
    return user_repo.get_all_users()


# ─── Get User by ID ───────────────────────────────────────────────────────────

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Return a single user by their ID."""
    user_repo = UserRepo(db)
    user = user_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

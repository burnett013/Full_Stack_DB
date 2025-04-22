from fastapi import APIRouter
from models.user_model import User
from services.user_service import create_user
from models.user_model import User
from typing import List

router = APIRouter()

@router.post("/users/")
def add_user(user: User):
    return create_user(user)


@router.get("/users/")
def get_users():
    # Temporary in-memory user list (replace with DB later)
    return [
        {
            "name": "Alice",
            "email": "alice@example.com",
            "certified": True,
            "login_time": "2025-04-18T10:00:00"
        },
        {
            "name": "Bob",
            "email": "bob@example.com",
            "certified": False,
            "login_time": "2025-04-18T11:30:00"
        }
    ]

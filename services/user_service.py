# services/user_service.py
from models.user_model import User

def create_user(user: User):
    return {"message": f"User {user.name} added.", "data": user.dict()}

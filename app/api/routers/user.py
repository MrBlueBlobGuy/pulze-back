from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from chats.users import add_user


router = APIRouter()

# In-memory storage for users (you can replace this with a database later)

class User(BaseModel):
    name: str
    phonenumber: str
    password: str



@router.post("/users/signup")
async def signup_user(user: User):
    return {
        "user":user,
        "status":200
    } if add_user(user.name, user.password) else {
        "status":400
    }

@router.post("/users/login")
async def login_user(user: User):
    return {
        "username":user.name,
        "status":200
    } if add_user(user.name, user.password) else {
        "status":400
    }

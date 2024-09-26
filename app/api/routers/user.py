from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from chats.users import add_user

import xmpp

router = APIRouter()

# In-memory storage for users (you can replace this with a database later)

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


@router.get("/users/login")
async def login_user(username:str, passw:str):
    return {
        "username":username,
        "status":200
    }

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from chats.users import add_user


router = APIRouter()

# In-memory storage for users (you can replace this with a database later)

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str



@router.get("/users/login")
async def login_user(username:str = Query(...), passw:str = Query(...)):
    return {
        "username":username,
        "status":200
    }
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from chats.users import add_user


router = APIRouter()

# In-memory storage for users (you can replace this with a database later)

class User(BaseModel):
    senderid:str
    receiverid:str
    message:str
    status:str
    timestamp:int
    messageid:str

@router.post("/messages/send")
async def send_message(message: User):
    return {
        "message":message,
        "status":200
    } if True else {
        "status":400
    }

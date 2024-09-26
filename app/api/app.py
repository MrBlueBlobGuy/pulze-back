#add users

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from .routers import user

app = FastAPI()

# In-memory storage for users (you can replace this with a database later)
app.include_router(user.router)

# Run the app with: uvicorn script_name:app --reload
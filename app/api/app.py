from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from asgiref.wsgi import WsgiToAsgi

from .routers import user

fastapi_app = FastAPI()

# In-memory storage for users (you can replace this with a database later)
fastapi_app.include_router(user.router)

# Wrap the FastAPI app with WsgiToAsgi
app = fastapi_app
from fastapi import FastAPI
from .routers import sulanuka

app = FastAPI()

app.include_router(sulanuka.router, prefix="/sulanuka", tags=["sulanuka"])
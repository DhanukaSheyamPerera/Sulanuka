from fastapi import FastAPI
from app.routers import sulanuka

app = FastAPI()

app.include_router(sulanuka.router, prefix="/api", tags=["Sulanuka"])
from fastapi import FastAPI, APIRouter, HTTPException

router = APIRouter()

@router.post("/encrypt")
async def encrypt():
    pass

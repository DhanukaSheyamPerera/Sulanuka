from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cryptography.fernet import Fernet

router = APIRouter()

key = Fernet.generate_key()
fernet = Fernet(key)

class Message(BaseModel):
    text: str

class EncryptedMessage(BaseModel):
    cipher: str
    key: str

@router.post("/encrypt", response_model=EncryptedMessage)
def encrypt_message(message: Message):
    try:
        encrypted_text = fernet.encrypt(message.text.encode())
        return {"cipher": encrypted_text.decode(), "key": key.decode()}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Encryption failed")

@router.post("/decrypt", response_model=Message)
def decrypt_message(cipher: str, key: str):
    try:
        fernet = Fernet(key.encode())
        decrypted_text = fernet.decrypt(cipher.encode()).decode()
        return {"text": decrypted_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Decryption failed")

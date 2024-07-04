from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.email_service import send_confirmation_email
from app.database import get_db, init_db
from app.models import User, create_user, confirm_user_email
from models import Base, engine, Session

app = FastAPI()

Base.metadata.create_all(bind=engine)


class EmailSchema(BaseModel):
    email: EmailStr


@app.post("/send-confirmation/")
async def send_confirmation(email_schema: EmailSchema, db: Session = Depends(get_db)):
    try:
        user = create_user(db, email_schema.email)
        send_confirmation_email(user.email, user.confirmation_token)
        return {"message": "Confirmation email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/confirm-email/")
async def confirm_email(token: str, db: Session = Depends(get_db)):
    user = confirm_user_email(db, token)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    return {"message": "Email confirmed successfully"}


# Initialize the database on startup
@app.on_event("startup")
async def startup():
    init_db()

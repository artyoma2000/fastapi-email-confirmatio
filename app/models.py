from sqlalchemy import Column, String, Boolean, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import uuid
from sqlalchemy import MetaData
from app.config import settings

Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)
metadata = MetaData()


class User(Base):
    __tablename__ = 'users'
    #id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор для каждой записи
    email = Column(String, primary_key=True, index=True)
    is_confirmed = Column(Boolean, default=False)
    confirmation_token = Column(String, unique=True, index=True)
    metadata = metadata


def create_user(db: Session, email: str):
    token = str(uuid.uuid4())
    user = User(email=email, confirmation_token=token)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def confirm_user_email(db: Session, token: str):
    try:
        user = db.query(User).filter(User.confirmation_token == token).first()
        if user and not user.is_confirmed:
            user.is_confirmed = True
            db.commit()
            return user
        return None
    except SQLAlchemyError:
        return None

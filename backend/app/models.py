from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")
from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from app.database import Base


class Users(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
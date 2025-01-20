from sqlalchemy import Column, Integer, String, DateTime, func
from .base_model import Base


class User(Base):
    __tablename__ = "users"

    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import BaseClass


class User(BaseClass):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True, nullable=True)
    password = Column(String)

    service_id = Column(Integer, ForeignKey("service.id"))

    service = relationship("Service", back_populates="users")

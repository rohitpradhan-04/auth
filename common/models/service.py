from ..database import Base
from sqlalchemy import Column, Integer, String
from ..database import BaseClass
from sqlalchemy.orm import relationship


class Service(BaseClass):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)

    users = relationship("User", back_populates="service")

from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .enum import Constants

db_connection = Constants()
database_url = f"postgresql://{db_connection.db_user}:{db_connection.db_password}@{db_connection.db_host}:{db_connection.db_port}/{db_connection.db_name}"


engin = create_engine(database_url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engin)


Base = declarative_base()


class BaseClass(Base):
    __abstract__ = True

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


def get_bd():
    db = session()
    try:
        yield db
    finally:
        db.close()

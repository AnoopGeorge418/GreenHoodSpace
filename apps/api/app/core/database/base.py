from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Creates sub classes of DeclarativeBase which will be mapped so that it represents a model/table."""

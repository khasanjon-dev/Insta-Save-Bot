from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Mapped, mapped_column


class CustomBase:
    # Generate __tablename__ automatically
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)

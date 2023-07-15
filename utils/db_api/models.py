from datetime import datetime

from sqlalchemy import (DateTime, Integer, String, func)
from sqlalchemy.orm import Mapped, mapped_column

from utils.db_api.db.base_class import Base


class Users(Base):
    first_name: Mapped[str] = mapped_column(String(250))
    last_name: Mapped[str] = mapped_column(String(250), nullable=True)
    username: Mapped[str] = mapped_column(String(250), unique=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=func.current_timestamp(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

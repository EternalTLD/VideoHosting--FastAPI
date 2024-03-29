"""Users models"""
import datetime
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base.models import BaseModel

from ..videos.models import *


class UserModel(BaseModel):
    __tablename__ = "users"

    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
    hashed_password: Mapped[str] = mapped_column()
    videos: Mapped[Optional[list["VideoModel"]]] = relationship(back_populates="user")

"""Videos models"""
import datetime
import uuid

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base.models import BaseModel

from ..users.models import *


class VideoModel(BaseModel):
    __tablename__ = "videos"

    title: Mapped[str]
    description: Mapped[str]
    filepath: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="videos")

from typing import TYPE_CHECKING, List

from core.db import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Contract,
        Task
    )


class Home(Base):
    __tablename__ = "home"

    address: Mapped[str] = mapped_column(primary_key=True)
    commisioning: Mapped[date] = mapped_column(nullable=True)
    floors: Mapped[int]
    index: Mapped[int]
    contracts: Mapped[List["Contract"]] = relationship(back_populates="home")
    tasks: Mapped[List["Task"]] = relationship(back_populates="home")

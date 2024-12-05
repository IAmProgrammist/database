from core.db import Base

from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy.sql.schema import ForeignKey

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Home,
        Resident,
        Payment,
        Worker
    )


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    payment: Mapped[int]
    completed_date: Mapped[date] = mapped_column(nullable=True)
    until_date: Mapped[date]
    home_address: Mapped[str] = mapped_column(
        ForeignKey("home.address", ondelete="restrict"), nullable=False
    )
    home: Mapped["Home"] = relationship(back_populates="tasks")
    workers: Mapped[List["Worker"]] = relationship(
        secondary="workers_tasks",
        back_populates="tasks"
    )

from core.db import Base

from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Task
    )


class Worker(Base):
    __tablename__ = "worker"

    inn: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    tasks: Mapped[List["Task"]] = relationship(
        secondary="workers_tasks",
        back_populates="workers"
    )

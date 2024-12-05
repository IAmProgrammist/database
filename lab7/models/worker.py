from core.db import Base

from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey, Table, Column

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Home,
        Resident,
        Payment,
        Task
    )

workers_tasks = Table(
    "workers_tasks",
    Base.metadata,
    Column("worker_inn", ForeignKey("worker.inn"), primary_key=True),
    Column("task_id", ForeignKey("task.id"), primary_key=True),
)


class Worker(Base):
    __tablename__ = "worker"

    inn: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    tasks: Mapped[List["Task"]] = relationship(
        secondary=workers_tasks,
        back_populates="workers"
    )

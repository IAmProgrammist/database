from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class WorkerTask(Base):
    __tablename__ = "workers_tasks"

    worker_inn: Mapped[str] = mapped_column(ForeignKey("worker.inn"), primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"), primary_key=True)

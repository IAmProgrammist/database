from datetime import date
from typing import Optional, Self

from pydantic import model_validator

from schemas.base import TunedModel


class TaskCreate(TunedModel):
    until_date: date
    completed_date: Optional[date]
    home_address: str


class TaskIdentifier(TunedModel):
    id: int


class TaskUpdate(TaskCreate):
    pass


class TaskShow(TaskCreate, TaskIdentifier):
    pass

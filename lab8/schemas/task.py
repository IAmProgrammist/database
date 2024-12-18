from datetime import date
from typing import Optional, Self

from pydantic import model_validator, field_validator

from schemas.base import TunedModel


class TaskCreate(TunedModel):
    until_date: date
    completed_date: Optional[date]
    home_address: str
    payment: int

    @field_validator("payment")
    def check_payment(cls, value):
        if value >= 0:
            return value

        raise ValueError("Плата должна быть положительной")


class TaskIdentifier(TunedModel):
    id: int


class TaskUpdate(TaskCreate):
    pass


class TaskShow(TaskCreate, TaskIdentifier):
    pass

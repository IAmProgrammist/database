from datetime import date
from typing import Optional, Self

from pydantic import model_validator, field_validator, EmailStr

from schemas.base import TunedModel, RuNumberType


class WorkerIdentifier(TunedModel):
    inn: str


class WorkerUpdate(TunedModel):
    email: Optional[EmailStr]
    phone: Optional[RuNumberType]


class WorkerCreate(WorkerUpdate, WorkerIdentifier):
    pass


class WorkerShow(WorkerCreate):
    pass

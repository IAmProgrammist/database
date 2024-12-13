from datetime import date
from typing import Optional, Self

from pydantic import model_validator, field_validator

from schemas.base import TunedModel


class PaymentIdentifier(TunedModel):
    id: str


class PaymentUpdate(TunedModel):
    paid_date: Optional[date]
    until_date: date
    contract_id: int
    energy_source: str
    payment: int

    @field_validator("payment")
    def check_payment(cls, value):
        if value >= 0:
            return value

        raise ValueError("Плата должна быть положительной")


class PaymentCreate(PaymentUpdate, PaymentIdentifier):
    pass


class PaymentShow(PaymentCreate):
    pass

from datetime import date
from typing import Optional, Self

from pydantic import model_validator

from schemas.base import TunedModel


class ContractCreate(TunedModel):
    transaction_date: date
    until_date: date
    home_address: str

    @model_validator(mode="after")
    def validate_dates(self) -> Self:
        if self.until_date > self.transaction_date:
            return self

        raise ValueError('Дата заключения договора не должна быть позже даты окончания договора')


class ContractIdentifier(TunedModel):
    id: int


class ContractUpdate(ContractCreate):
    pass


class ContractShow(ContractCreate, ContractIdentifier):
    pass

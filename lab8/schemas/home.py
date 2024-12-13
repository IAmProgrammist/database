from datetime import date
from typing import Optional, Self

from pydantic import model_validator, field_validator

from schemas.base import TunedModel


class HomeIdentifier(TunedModel):
    address: str


class HomeUpdate(TunedModel):
    commisioning: Optional[date]
    floors: int
    index: int

    @field_validator("floors")
    def check_floors(cls, value):
        if value > 0:
            return value

        raise ValueError("В доме не может быть < 0 этажей")

    @field_validator("index")
    def check_index(cls, value):
        if 100_000 <= value <= 999_999:
            return value

        raise ValueError("Индекс должен быть в районе от 100000 до 999999")


class HomeCreate(HomeUpdate, HomeIdentifier):
    pass


class HomeShow(HomeCreate):
    pass

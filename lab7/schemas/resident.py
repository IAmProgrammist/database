from typing import Optional
from pydantic import field_validator
from schemas.base import TunedModel, RuNumberType
from pydantic import EmailStr
import re


class ResidentIdentifier(TunedModel):
    passport_data: str

    @field_validator("passport_data", mode="after")
    def validate_passport_data(cls, value):
        if not re.match(r"^\d{10}$", value):
            raise ValueError("Паспортные данные должны содержать 10 цифр, 4 первые - серия, 6 остальных - номер паспорта")
        return value


class ResidentUpdate(TunedModel):
    surname: str
    name: str
    patronymics: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[RuNumberType]

    @field_validator("surname", "name", mode="after")
    def validate_surname_name(cls, value):
        if not re.match(r"^[А-ЯЁа-яёA-Za-z-]+$", value):
            raise ValueError("Фамилия и имя должны содержать латинские, кириллические символы и дефис, они не должны быть пустыми")
        return value

    @field_validator("surname", "name", mode="after")
    def validate_patronymics(cls, value):
        if value is None:
            return value

        if not re.match(r"^[А-ЯЁа-яёA-Za-z-]+$", value):
            raise ValueError("Отчество должно содержать латинские, кириллические символы и дефис")

        return value

class ResidentCreate(ResidentUpdate, ResidentIdentifier):
    pass


class ResidentShow(ResidentCreate):
    pass

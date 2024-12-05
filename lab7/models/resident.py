from typing import TYPE_CHECKING, List

from sqlalchemy import Table, Column, ForeignKey

from core.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Contract
    )

residents_contracts = Table(
    "residents_contracts",
    Base.metadata,
    Column("resident_passport_data", ForeignKey("resident.passport_data"), primary_key=True),
    Column("contract_id", ForeignKey("contract.id"), primary_key=True),
)


class Resident(Base):
    __tablename__ = "resident"

    passport_data: Mapped[str] = mapped_column(primary_key=True)
    surname: Mapped[str]
    name: Mapped[str]
    patronymics: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    contracts: Mapped[List["Contract"]] = relationship(
        secondary=residents_contracts
    )

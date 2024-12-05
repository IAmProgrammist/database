from core.db import Base

from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy.sql.schema import ForeignKey

from models.resident import residents_contracts

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Home,
        Resident,
        Payment
    )


class Contract(Base):
    __tablename__ = "contract"

    id: Mapped[int] = mapped_column(primary_key=True)
    transaction_date: Mapped[date]
    until_date: Mapped[date]
    payment: Mapped[int]
    home_address: Mapped[str] = mapped_column(
        ForeignKey("home.address", ondelete="restrict"), nullable=False
    )
    home: Mapped["Home"] = relationship(back_populates="contracts")
    residents: Mapped[List["Resident"]] = relationship(
        secondary=residents_contracts
    )
    payments: Mapped[List["Payment"]] = relationship(back_populates="contract")

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey

from core.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Contract
    )


class Payment(Base):
    __tablename__ = "payment"

    id: Mapped[str] = mapped_column(primary_key=True)
    paid_date: Mapped[date] = mapped_column(nullable=True)
    until_date: Mapped[date]
    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id", ondelete="set null"), nullable=True)
    contract: Mapped["Contract"] = relationship(back_populates="payments")
    energy_source: Mapped[str] = mapped_column(server_default="Undefined")
    payment: Mapped[int]

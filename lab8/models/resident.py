from typing import TYPE_CHECKING, List
from core.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import (  # noqa: F401
        Contract
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
        secondary="residents_contracts",
        back_populates="residents"
    )

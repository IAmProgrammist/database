from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class ResidentContract(Base):
    __tablename__ = "residents_contracts"

    resident_passport_data: Mapped[str] = mapped_column(ForeignKey("resident.passport_data"), primary_key=True)
    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"), primary_key=True)

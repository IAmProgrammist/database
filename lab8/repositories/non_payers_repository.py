from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.orm import Session

from core.db import engine
from dto import NonPayersDTOGenerator
from models import Resident, Payment, Contract, ResidentContract
from repositories.base import Repository


class NonPayersRepository(Repository):
    def __init__(self):
        super().__init__(None, NonPayersDTOGenerator())

    def select(self):
        select_model = self.generator.select()
        if select_model is None:
            raise NotImplementedError(f"Выбрать из {self._table.__tablename__} невозможно")

        with Session(engine) as session:
            results = session.execute(
                select(
                    func.concat(Resident.surname, " ", Resident.name, " ", Resident.patronymics).label("snp"),
                    func.sum(Payment.payment).label("debt"),
                    Payment.energy_source
                )
                .select_from(Resident)
                .join(ResidentContract, ResidentContract.resident_passport_data == Resident.passport_data)
                .join(Contract)
                .join(Payment)
                .where(Payment.paid_date.is_(None))
                .group_by(Resident.passport_data, Payment.energy_source)
                .order_by("debt")
            ).all()
            return [select_model.model_validate({"snp": result[0], "debt": result[1], "energy_source": result[2]}) for result in results]

    def insert(self, data: dict) -> None:
        return super().insert(data)

    def update(self, data: dict, identifier: dict) -> None:
        return super().update(data, identifier)

    def delete(self, identifier: dict) -> None:
        return super().delete(identifier)

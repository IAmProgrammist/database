from sqlalchemy import select, func, text
from sqlalchemy.orm import Session

from core.db import engine
from dto import HomeProfitDTOGenerator
from models import Home, Contract, Payment, Task
from repositories.base import Repository


class ProfitHouseRepository(Repository):
    def __init__(self):
        super().__init__(None, HomeProfitDTOGenerator())

    def select(self):
        select_model = self.generator.select()
        if select_model is None:
            raise NotImplementedError(f"Выбрать из {self._table.__tablename__} невозможно")

        with Session(engine) as session:
            plus = (select(
                Contract.home_address.label("home"),
                func.sum(Payment.payment).label("plus")
            )
                    .select_from(Payment)
                    .join(Contract, isouter=True)
                    .group_by(Contract.home_address)
                    .subquery())

            minus = (select(
                Task.home_address.label("home"),
                func.sum(Task.payment).label("minus")
            )
                     .select_from(Task)
                     .group_by(Task.home_address)
                     .subquery())

            main_query = (select(
                    Home.address.label("address"),
                    (
                            func.coalesce(plus.c.plus, 0) - func.coalesce(minus.c.minus, 0)
                    ).label("profit")
                ).select_from(Home)
                 .join(plus, plus.c.home == Home.address, isouter=True)
                 .join(minus, minus.c.home == Home.address, isouter=True)
                 .order_by("profit"))

            results = session.execute(
                main_query
            ).all()

            explain = session.execute(
                text(f"EXPLAIN ANALYZE {main_query.compile(compile_kwargs={'literal_binds': True})}")).all()
            print("EXPLAIN ANALYZE of house profit")
            for line in explain:
                print(line[0])

            return [select_model.model_validate({"address": result[0], "profit": result[1]}) for result in results]

    def insert(self, data: dict) -> None:
        return super().insert(data)

    def update(self, data: dict, identifier: dict) -> None:
        return super().update(data, identifier)

    def delete(self, identifier: dict) -> None:
        return super().delete(identifier)

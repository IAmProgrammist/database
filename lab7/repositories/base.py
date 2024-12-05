from sqlalchemy import select, ScalarResult, and_
from tabulate import tabulate
from typing import Any

from core.db import engine
from dto.base import BaseDTOGeneartor
from sqlalchemy.orm import Session

from schemas.base import TunedModel


class Repository:
    def __init__(self, table, generator: BaseDTOGeneartor):
        self._table = table
        self.generator = generator

    def get_dto_generator(self):
        return self.generator

    def select(self) -> list[TunedModel]:
        select_model = self.generator.select()
        if select_model is None:
            raise NotImplementedError(f"Выбрать из {self._table.__tablename__} невозможно")

        with Session(engine) as session:
            results = session.execute(select(self._table)).all()
            return [select_model.model_validate(result[0]) for result in results]

    def insert(self, data: dict) -> None:
        select_model = self.generator.insert()
        if select_model is None:
            raise NotImplementedError(f"Вставить в {self._table.__tablename__} невозможно")

        insert_data = select_model(**data)

        with Session(engine) as session:
            new_object = self._table(**insert_data.dict())
            session.add(new_object)
            session.commit()

    def update(self, data: dict, identifier: dict) -> None:
        update_model = self.generator.update()
        identifier_model = self.generator.identifier()
        if update_model is None or identifier_model is None:
            raise NotImplementedError(f"Обновить {self._table.__tablename__} невозможно")

        update_data = update_model(**data)
        identifier_data = identifier_model(**identifier)

        with Session(engine) as session:
            object = session.execute(select(self._table).filter(
                and_(
                    *(list(map(lambda x: getattr(self._table, x[0]) == x[1], identifier_data.model_dump().items())))
                )
            )).one_or_none()

            if not object:
                raise LookupError(f"Элемент {self._table.__tablename__} с {identifier_data.model_dump()} невозможно найти")

            object = object[0]

            for key, value in update_data.model_dump().items():
                setattr(object, key, value)

            session.commit()

    def delete(self, identifier: dict) -> None:
        identifier_model = self.generator.identifier()
        if identifier_model is None:
            raise NotImplementedError(f"Удалить {self._table.__tablename__} невозможно")

        identifier_data = identifier_model(**identifier)

        with Session(engine) as session:
            object = session.execute(select(self._table).filter(
                and_(
                    *(list(map(lambda x: getattr(self._table, x[0]) == x[1], identifier_data.model_dump().items())))
                )
            )).one_or_none()

            if not object:
                raise LookupError(
                    f"Элемент {self._table.__tablename__} с {identifier_data.model_dump()} невозможно найти")

            object = object[0]

            session.delete(object)
            session.commit()

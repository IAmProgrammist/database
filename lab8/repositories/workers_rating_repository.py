from sqlalchemy import select, func, and_, desc, text
from sqlalchemy.orm import Session

from core.db import engine
from dto import WorkrsRatingDTOGenerator
from models import Worker, WorkerTask, Task
from repositories.base import Repository


class WorkersRatingRepository(Repository):
    def __init__(self):
        super().__init__(None, WorkrsRatingDTOGenerator())

    def select(self):
        select_model = self.generator.select()
        if select_model is None:
            raise NotImplementedError(f"Выбрать из {self._table.__tablename__} невозможно")

        with Session(engine) as session:
            begin_date = '2004-01-01'
            end_date = '2040-01-01'

            completed_total = (
                select(
                    WorkerTask.worker_inn,
                    func.count().label("total"),
                    func.count(Task.completed_date).label("completed")
                )
                .select_from(WorkerTask)
                .join(Task)
                .where(
                    Task.until_date.between(begin_date, end_date)
                )
                .group_by(WorkerTask.worker_inn)
            ).subquery()

            main_query = (select(
                    Worker.inn.label("worker_inn"),
                    func.coalesce(completed_total.c.completed, 0).label("completed"),
                    (1.0 * func.coalesce(completed_total.c.completed, 0) / func.coalesce(completed_total.c.total, 1)).label("rating")
                )
                .select_from(Worker)
                .join(completed_total, completed_total.c.worker_inn == Worker.inn, isouter=True)
                .order_by(desc("completed")))

            results = session.execute(
                main_query
            )

            explain = session.execute(text(f"EXPLAIN ANALYZE {main_query.compile(compile_kwargs={'literal_binds': True})}")).all()
            print("EXPLAIN ANALYZE of workers rating")
            for line in explain:
                print(line[0])

            return [select_model.model_validate({"inn": result[0], "completed": result[1], "rating": result[2]}) for result in results]

    def insert(self, data: dict) -> None:
        return super().insert(data)

    def update(self, data: dict, identifier: dict) -> None:
        return super().update(data, identifier)

    def delete(self, identifier: dict) -> None:
        return super().delete(identifier)

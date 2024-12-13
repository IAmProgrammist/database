from sqlalchemy import select, func, and_, desc
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

            completed = (
                select(
                    WorkerTask.worker_inn,
                    func.count().label("completed")
                )
                .select_from(WorkerTask)
                .join(Task)
                .where(
                    and_(
                        Task.completed_date.isnot(None),
                        Task.until_date > begin_date,
                        Task.until_date < end_date
                    )
                )
                .group_by(WorkerTask.worker_inn)
            ).subquery()

            total = (
                select(
                    WorkerTask.worker_inn,
                    func.count().label("total")
                )
                .select_from(WorkerTask)
                .join(Task)
                .where(
                    and_(
                        Task.until_date > begin_date,
                        Task.until_date < end_date
                    )
                )
                .group_by(WorkerTask.worker_inn)
            ).subquery()

            results = session.execute(
                select(
                    Worker.inn.label("worker_inn"),
                    func.coalesce(completed.c.completed, 0).label("completed"),
                    (1.0 * func.coalesce(completed.c.completed, 0) / total.c.total).label("rating")
                )
                .select_from(Worker)
                .join(completed, completed.c.worker_inn == Worker.inn, isouter=True)
                .join(total, total.c.worker_inn == Worker.inn)
                .order_by(desc("completed"))
            )

            return [select_model.model_validate({"inn": result[0], "completed": result[1], "rating": result[2]}) for result in results]

    def insert(self, data: dict) -> None:
        return super().insert(data)

    def update(self, data: dict, identifier: dict) -> None:
        return super().update(data, identifier)

    def delete(self, identifier: dict) -> None:
        return super().delete(identifier)

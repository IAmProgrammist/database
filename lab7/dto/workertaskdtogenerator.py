from dto.base import BaseDTOGeneartor
from schemas.workertasks import WorkerTasksIdentifier, WorkerTasksShow, WorkerTasksCreate


class WorkerTaskDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "worker_inn": "ИНН исполнителя",
            "task_id": "Ид. ном. работы"
        }

    def select(self):
        return WorkerTasksShow

    def insert(self):
        return WorkerTasksCreate

    def update(self):
        return None

    def identifier(self):
        return WorkerTasksIdentifier

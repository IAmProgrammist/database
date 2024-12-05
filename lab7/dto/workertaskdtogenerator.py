from dto.base import BaseDTOGeneartor


class WorkerTaskDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "worker_inn": "ИНН исполнителя",
            "task_id": "Ид. ном. работы"
        }

    def insert(self):
        return {
            "worker_inn": None,
            "task_id": None
        }

    def select(self):
        return ["worker_inn", "task_id"]

    def update(self):
        return {
        }

    def identifier(self):
        return {
            "worker_inn": None,
            "task_id": None
        }

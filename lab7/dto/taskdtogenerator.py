from dto.base import BaseDTOGeneartor
from schemas.task import TaskCreate, TaskUpdate, TaskIdentifier, TaskShow


class TaskDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "id": "Идентификационный номер",
            "completed_date": "Дата окончания",
            "until_date": "Дедлайн",
            "home_address": "Дом",
        }

    def select(self):
        return TaskShow

    def insert(self):
        return TaskCreate

    def update(self):
        return TaskUpdate

    def identifier(self):
        return TaskIdentifier

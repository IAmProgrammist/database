from dto.base import BaseDTOGeneartor
from schemas.worker import WorkerCreate, WorkerUpdate, WorkerIdentifier, WorkerShow


class WorkerDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "inn": "ИНН",
            "email": "Электронная почта",
            "phone": "Номер телефона"
        }

    def select(self):
        return WorkerShow

    def insert(self):
        return WorkerCreate

    def update(self):
        return WorkerUpdate

    def identifier(self):
        return WorkerIdentifier

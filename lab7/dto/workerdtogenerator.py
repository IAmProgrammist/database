from dto.base import BaseDTOGeneartor


class WorkerDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "inn": "ИНН",
            "email": "Электронная почта",
            "phone": "Номер телефона"
        }

    def insert(self):
        return {
            "inn": None,
            "email": None,
            "phone": None
        }

    def select(self):
        return ["inn", "email", "phone"]

    def update(self):
        return {
            "email": None,
            "phone": None
        }

    def identifier(self):
        return {
            "inn": None,
        }

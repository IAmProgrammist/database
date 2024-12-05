from dto.base import BaseDTOGeneartor


class TaskDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "id": "Идентификационный номер",
            "completed_date": "Дата окончания",
            "until_date": "Дедлайн",
            "home": "Дом",
        }

    def insert(self):
        return {
            "completed_date": None,
            "until_date": None,
            "home": None
        }

    def select(self):
        return ["id", "completed_date", "until_date", "home"]

    def update(self):
        return {
            "completed_date": None,
            "until_date": None,
            "home": None
        }

    def identifier(self):
        return {
            "id": None,
        }

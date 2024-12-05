from lab6.dto.base import BaseDTOGeneartor


class WorkrsRatingDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "inn": "ИНН Рабочего",
            "completed": "Завершено работ",
            "rating": "Рейтинг"
        }

    def insert(self):
        return {}

    def select(self):
        return ["inn", "completed", "rating"]

    def update(self):
        return {}

    def identifier(self):
        return {}

from dto.base import BaseDTOGeneartor
from schemas.reports import WorkersRatingReportShow


class WorkrsRatingDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "inn": "ИНН Рабочего",
            "completed": "Завершено работ",
            "rating": "Рейтинг"
        }

    def select(self):
        return WorkersRatingReportShow

    def insert(self):
        return None

    def update(self):
        return None

    def identifier(self):
        return None

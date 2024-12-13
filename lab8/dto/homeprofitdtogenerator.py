from dto.base import BaseDTOGeneartor
from schemas.reports import HomeProfitReportShow


class HomeProfitDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "address": "Адрес",
            "profit": "Прибыль"
        }

    def select(self):
        return HomeProfitReportShow

    def insert(self):
        return None

    def update(self):
        return None

    def identifier(self):
        return None

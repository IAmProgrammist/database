from dto.base import BaseDTOGeneartor


class HomeProfitDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "address": "Адрес",
            "profit": "Прибыль"
        }

    def insert(self):
        return {}

    def select(self):
        return ["address", "profit"]

    def update(self):
        return {}

    def identifier(self):
        return {}

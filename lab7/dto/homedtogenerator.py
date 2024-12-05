from dto.base import BaseDTOGeneartor


class HomeDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "address": "Адрес",
            "commisioning": "Дата введения в эксплуатацию",
            "floors": "Этажность",
            "index": "Индекс"
        }

    def insert(self):
        return {
            "address": None,
            "commisioning": None,
            "floors": None,
            "index": None
        }

    def select(self):
        return ["address", "commisioning", "floors", "index"]

    def update(self):
        return {
            "commisioning": None,
            "floors": None,
            "index": None
        }

    def identifier(self):
        return {
            "address": None
        }

from dto.base import BaseDTOGeneartor
from schemas.home import HomeCreate, HomeUpdate, HomeIdentifier, HomeShow


class HomeDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "address": "Адрес",
            "commisioning": "Дата введения в эксплуатацию",
            "floors": "Этажность",
            "index": "Индекс"
        }

    def select(self):
        return HomeShow

    def insert(self):
        return HomeCreate

    def update(self):
        return HomeUpdate

    def identifier(self):
        return HomeIdentifier

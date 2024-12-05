from dto.base import BaseDTOGeneartor
from schemas.resident import ResidentCreate, ResidentUpdate, ResidentIdentifier, ResidentShow


class ResidentDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "passport_data": "Паспортные данные",
            "surname": "Фамилия",
            "name": "Имя",
            "patronymics": "Отчество",
            "email": "Электронная почта",
            "phone": "Номер телефона",
        }

    def select(self):
        return ResidentShow

    def insert(self):
        return ResidentCreate

    def update(self):
        return ResidentUpdate

    def identifier(self):
        return ResidentIdentifier

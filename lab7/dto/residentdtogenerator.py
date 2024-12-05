from dto.base import BaseDTOGeneartor


class ResidentDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "passport_data": "Паспортные данные",
            "snp": "ФИО",
            "email": "Электронная почта",
            "phone": "Номер телефона",
        }

    def insert(self):
        return {
            "passport_data": None,
            "snp": None,
            "email": None,
            "phone": None
        }

    def select(self):
        return ["passport_data", "snp", "email", "phone"]

    def update(self):
        return {
            "snp": None,
            "email": None,
            "phone": None
        }

    def identifier(self):
        return {
            "passport_data": None,
        }

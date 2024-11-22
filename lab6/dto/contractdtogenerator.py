from lab6.dto.base import BaseDTOGeneartor


class ContractDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "transaction_date": "Дата начала",
            "until_date": "Дата окончания",
            "home": "Дом",
            "id": "Идентификационный номер"
        }

    def insert(self):
        return {
            "home": None,
            "until_date": None,
            "transaction_date": None
        }

    def select(self):
        return ["id", "home", "until_date", "transaction_date"]

    def update(self):
        return {
            "home": None,
            "until_date": None,
            "transaction_date": None
        }

    def identifier(self):
        return {
            "id": None
        }

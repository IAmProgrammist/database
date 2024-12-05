from dto.base import BaseDTOGeneartor
from schemas.contract import ContractCreate, ContractUpdate, ContractIdentifier, ContractShow


class ContractDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "transaction_date": "Дата начала",
            "until_date": "Дата окончания",
            "home_address": "Дом",
            "id": "Идентификационный номер"
        }

    def select(self):
        return ContractShow

    def insert(self):
        return ContractCreate

    def update(self):
        return ContractUpdate

    def identifier(self):
        return ContractIdentifier

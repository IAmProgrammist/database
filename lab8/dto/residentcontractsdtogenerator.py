from dto.base import BaseDTOGeneartor
from schemas.residentcontracts import ResidentContractCreate, ResidentContractIdentifier, ResidentContractShow


class ResidentContractDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "resident_passport_data": "Паспортные данные",
            "contract_id": "Ид. ном. договора",
        }

    def select(self):
        return ResidentContractShow

    def insert(self):
        return ResidentContractCreate

    def update(self):
        return None

    def identifier(self):
        return ResidentContractIdentifier

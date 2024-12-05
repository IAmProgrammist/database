from dto.base import BaseDTOGeneartor


class ResidentContractDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "resident_passport_data": "Паспортные данные",
            "contract_id": "Ид. ном. договора",
        }

    def insert(self):
        return {
            "resident_passport_data": None,
            "contract_id": None
        }

    def select(self):
        return ["resident_passport_data", "contract_id"]

    def update(self):
        return {
        }

    def identifier(self):
        return {
            "resident_passport_data": None,
            "contract_id": None
        }

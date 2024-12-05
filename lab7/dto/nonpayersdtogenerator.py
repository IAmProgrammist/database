from dto.base import BaseDTOGeneartor


class NonPayersDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "snp": "ФИО",
            "debt": "Долг",
            "energy_source": "Энергетический ресурс"
        }

    def insert(self):
        return {}

    def select(self):
        return ["snp", "debt", "energy_source"]

    def update(self):
        return {}

    def identifier(self):
        return {}

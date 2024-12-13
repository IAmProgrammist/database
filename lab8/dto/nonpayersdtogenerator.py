from dto.base import BaseDTOGeneartor
from schemas.reports import NonPayersReportShow


class NonPayersDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "snp": "ФИО",
            "debt": "Долг",
            "energy_source": "Энергетический ресурс"
        }

    def select(self):
        return NonPayersReportShow

    def insert(self):
        return None

    def update(self):
        return None

    def identifier(self):
        return None

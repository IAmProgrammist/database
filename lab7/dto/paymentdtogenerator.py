from dto.base import BaseDTOGeneartor


class PaymentDTOGenerator(BaseDTOGeneartor):
    def translations(self):
        return {
            "id": "УИП",
            "paid_date": "Дата оплаты",
            "until_date": "Срок оплаты",
            "contract_id": "Ид. ном. договора",
            "energy_source": "Энергетический ресурс",
            "payment": "Сумма"
        }

    def insert(self):
        return {
            "id": None,
            "paid_date": None,
            "until_date": None,
            "contract_id": None,
            "energy_source": None,
            "payment": None
        }

    def select(self):
        return ["id", "paid_date", "until_date", "contract_id", "energy_source", "payment"]

    def update(self):
        return {
            "paid_date": None,
            "until_date": None,
            "contract_id": None,
            "energy_source": None,
            "payment": None
        }

    def identifier(self):
        return {
            "id": None,
        }

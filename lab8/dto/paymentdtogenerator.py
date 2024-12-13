from dto.base import BaseDTOGeneartor
from schemas.payment import PaymentCreate, PaymentUpdate, PaymentIdentifier, PaymentShow


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

    def select(self):
        return PaymentShow

    def insert(self):
        return PaymentCreate

    def update(self):
        return PaymentUpdate

    def identifier(self):
        return PaymentIdentifier

from schemas.base import TunedModel


class ResidentContractIdentifier(TunedModel):
    resident_passport_data: str
    contract_id: int


class ResidentContractCreate(ResidentContractIdentifier):
    pass


class ResidentContractShow(ResidentContractIdentifier):
    pass

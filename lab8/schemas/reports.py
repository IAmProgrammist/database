from schemas.base import TunedModel


class HomeProfitReportShow(TunedModel):
    address: str
    profit: int


class NonPayersReportShow(TunedModel):
    snp: str
    debt: int
    energy_source: str


class WorkersRatingReportShow(TunedModel):
    inn: str
    completed: int
    rating: float

from dto import ContractDTOGenerator, HomeDTOGenerator, PaymentDTOGenerator, ResidentDTOGenerator, \
    ResidentContractDTOGenerator, TaskDTOGenerator, WorkerDTOGenerator, WorkerTaskDTOGenerator
from models import Contract, Home, Payment, Resident, Task, Worker, WorkerTask, ResidentContract
from repositories.base import Repository
from repositories.non_payers_repository import NonPayersRepository
from repositories.profit_house_repository import ProfitHouseRepository
from repositories.workers_rating_repository import WorkersRatingRepository

contract_repository = Repository(Contract, ContractDTOGenerator())
home_repository = Repository(Home, HomeDTOGenerator())
payment_repository = Repository(Payment, PaymentDTOGenerator())
resident_repository = Repository(Resident, ResidentDTOGenerator())
residents_contracts_repository = Repository(ResidentContract, ResidentContractDTOGenerator())
task_repository = Repository(Task, TaskDTOGenerator())
worker_repository = Repository(Worker, WorkerDTOGenerator())
workers_tasks_repository = Repository(WorkerTask, WorkerTaskDTOGenerator())
non_payers_repository = NonPayersRepository()
workers_rating_repository = WorkersRatingRepository()
profit_house_repository = ProfitHouseRepository()

all_repos = [
    {"repo": contract_repository, "name": "Договоры"},
    {"repo": home_repository, "name": "Дома"},
    {"repo": payment_repository, "name": "Чеки"},
    {"repo": resident_repository, "name": "Жильцы"},
    {"repo": residents_contracts_repository, "name": "Договоры жильцов"},
    {"repo": task_repository, "name": "Работы"},
    {"repo": worker_repository, "name": "Исполнители работ"},
    {"repo": workers_tasks_repository, "name": "Назначения работ"},
    {"repo": non_payers_repository, "name": "Жильцы-неплательщики"},
    {"repo": workers_rating_repository, "name": "Рейтинг рабочих"},
    {"repo": profit_house_repository, "name": "Прибыль домов"}
]

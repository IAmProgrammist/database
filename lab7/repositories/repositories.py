from os import getenv
import psycopg2

from lab6.dto import ContractDTOGenerator, HomeDTOGenerator, PaymentDTOGenerator, ResidentDTOGenerator, \
    ResidentContractDTOGenerator, TaskDTOGenerator, WorkerDTOGenerator, WorkerTaskDTOGenerator, NonPayersDTOGenerator, \
    WorkrsRatingDTOGenerator, HomeProfitDTOGenerator
from lab6.repositories.base import Repository
from lab6.repositories.non_payers_repository import NonPayersRepository
from lab6.repositories.profit_house_repository import ProfitHouseRepository
from lab6.repositories.workers_rating_repository import WorkersRatingRepository

connection = psycopg2.connect(database=getenv("DATABASE"),
                              user=getenv("USERNAME"),
                              password=getenv("PASSWORD"),
                              host=getenv("HOST"),
                              port=int(getenv("PORT")),
                              options=f"-c search_path={getenv('SCHEMA')}"
                              )

contract_repository = Repository(connection, "contract", ContractDTOGenerator())
home_repository = Repository(connection, "home", HomeDTOGenerator())
payment_repository = Repository(connection, "payment", PaymentDTOGenerator())
resident_repository = Repository(connection, "resident", ResidentDTOGenerator())
residents_contracts_repository = Repository(connection, "residents_contracts", ResidentContractDTOGenerator())
task_repository = Repository(connection, "task", TaskDTOGenerator())
worker_repository = Repository(connection, "worker", WorkerDTOGenerator())
workers_tasks_repository = Repository(connection, "workers_tasks", WorkerTaskDTOGenerator())
non_payers_repository = NonPayersRepository(connection, NonPayersDTOGenerator())
workers_rating_repository = WorkersRatingRepository(connection, WorkrsRatingDTOGenerator())
profit_house_repository = ProfitHouseRepository(connection, HomeProfitDTOGenerator())

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

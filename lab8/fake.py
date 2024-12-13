import sys

from PySide6.QtWidgets import QApplication
from sqlalchemy.orm import Session

from core.db import engine
from models import Home, Contract, Resident, Payment, Task, Worker
from faker import Faker
from datetime import date, timedelta
from widgets.main import MainDialog
import random

MAX_COUNT = 100

homes = []
contracts = []
residents = []
payments = []
tasks = []
workers = []

if __name__ == "__main__":
    fake = Faker()
    with Session(engine) as session:
        print("Generating homes...")
        for i in range(0, MAX_COUNT):
            new_home = Home(
                address=fake.address(),
                commisioning=fake.date_between(
                    start_date=(date.today() + timedelta(days=500)),
                    end_date=(date.today() + timedelta(days=1000))),
                floors=fake.random_int(1, 50),
                index=fake.random_int(100000, 999999)
            )

            session.add(new_home)
            session.commit()
            homes.append(new_home)

        print("Generating contracts...")
        for i in range(0, MAX_COUNT):
            new_contract = Contract(
                transaction_date=fake.date_between(
                    start_date=(date.today() + timedelta(days=500)),
                    end_date=(date.today() + timedelta(days=1000))),
                until_date=fake.date_between(
                    start_date=(date.today() + timedelta(days=1001)),
                    end_date=(date.today() + timedelta(days=1500))),
                home_address=random.choice(homes).address
            )

            session.add(new_contract)
            session.commit()
            contracts.append(new_contract)

        prefix_phone = [
            "+7921",
            "+7931",
            "+7911",
            "+7953",
            "+7995",
            "+7912",
            "+7991",
            "+7999",
            "+7956",
            "+7900",
        ]

        print("Generating residents...")
        for i in range(0, MAX_COUNT):
            new_resident = Resident(
                passport_data=str(fake.random_int(1000_000000, 9999_999999)),
                surname=fake.last_name(),
                name=fake.first_name(),
                patronymics=fake.first_name() if random.random() > 0.5 else None,
                email=fake.email(),
                phone=f"{random.choice(prefix_phone)}{random.randint(100, 999)}{random.randint(1000, 9999)}",
                contracts=random.sample(contracts, fake.random_int(0, 2))
            )

            session.add(new_resident)
            session.commit()
            residents.append(new_resident)

        energy_sources = [
            "Ремонт",
            "Интернет",
            "Вода",
            "Электричество",
            "Отопление"
        ]

        print("Generating payments...")
        for i in range(0, MAX_COUNT):
            new_payment = Payment(
                id=str(fake.random_int(1000000000000, 10000000000000)),
                until_date=fake.date_between(
                    start_date=(date.today() - timedelta(days=300)),
                    end_date=(date.today() - timedelta(days=200))),
                paid_date=fake.date_between(
                    start_date=(date.today() - timedelta(days=400)),
                    end_date=(date.today() - timedelta(days=100))) if random.random() > 0.5 else None,
                contract_id=random.choice(contracts).id,
                energy_source=random.choice(energy_sources),
                payment=fake.random_int(100, 10001)
            )

            session.add(new_payment)
            session.commit()
            payments.append(new_payment)

        print("Generating tasks...")
        for i in range(0, MAX_COUNT):
            new_task = Task(
                payment=fake.random_int(100_000, 10_000_000),
                until_date=fake.date_between(
                    start_date=(date.today() - timedelta(days=300)),
                    end_date=(date.today() - timedelta(days=200))),
                completed_date=fake.date_between(
                    start_date=(date.today() - timedelta(days=400)),
                    end_date=(date.today() - timedelta(days=100))) if random.random() > 0.5 else None,
                home_address=random.choice(homes).address
            )

            session.add(new_task)
            session.commit()
            tasks.append(new_task)

        print("Generating tasks...")
        for i in range(0, MAX_COUNT):
            new_worker = Worker(
                inn=str(fake.random_int(100_000_000_000, 1_000_000_000_000)),
                email=fake.email() if random.random() < 0.5 else None,
                phone=f"{random.choice(prefix_phone)}{random.randint(100, 999)}{random.randint(1000, 9999)}" if random.random() < 0.5 else None,
                tasks=random.sample(tasks, fake.random_int(0, 10))
            )

            session.add(new_worker)
            session.commit()
            workers.append(new_worker)

        print("Done!")
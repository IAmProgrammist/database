from repositories.base import Repository


class NonPayersRepository(Repository):
    def __init__(self, connection, dtogenerator):
        super().__init__(connection, "", dtogenerator)

    def select(self, keys: list[str]):
        with self.connection.cursor() as cursor:

            try:
                cursor.execute(f'''
SELECT 
  resident.snp, 
  SUM(payment.payment) AS debt, 
  payment.energy_source 
FROM 
  resident 
  INNER JOIN residents_contracts ON residents_contracts.resident_passport_data = resident.passport_data 
  INNER JOIN contract ON residents_contracts.contract_id = contract.id 
  INNER JOIN payment ON payment.contract_id = contract.id 
WHERE 
  payment.paid_date IS NULL 
GROUP BY 
  resident.passport_data, 
  payment.energy_source 
ORDER BY 
  debt DESC;
''')
                result = []

                for row in cursor.fetchall():
                    i = 0
                    new_element = dict()
                    for key in keys:
                        new_element[key] = row[i]
                        i += 1

                    result.append(new_element)

                return result
            except Exception as e:
                self.connection.rollback()
                raise e

    def insert(self, data: dict) -> None:
        raise ModuleNotFoundError("Невозможно добавить элементы в отчёт")

    def update(self, data: dict, identifier: dict) -> None:
        raise ModuleNotFoundError("Невозможно обновить элементы в отчёте")

    def delete(self, identifier: dict) -> None:
        raise ModuleNotFoundError("Невозможно удалить элемент в отчёте")

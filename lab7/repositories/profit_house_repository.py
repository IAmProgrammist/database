from lab6.repositories.base import Repository


class ProfitHouseRepository(Repository):
    def __init__(self, connection, dtogenerator):
        super().__init__(connection, "", dtogenerator)

    def select(self, keys: list[str]):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f'''
SELECT 
  home.address as address, 
  (
    COALESCE(t1.plus, 0) - COALESCE(t2.minus, 0)
  ) as profit 
FROM 
  home 
  LEFT JOIN (
    SELECT 
      contract.home AS home, 
      SUM(payment.payment) as plus 
    FROM 
      payment 
      LEFT JOIN contract ON contract.id = payment.contract_id 
    GROUP BY 
      contract.home
  ) as t1 ON t1.home = address 
  LEFT JOIN (
    SELECT 
      task.home AS home, 
      SUM(task.payment) as minus 
    FROM 
      task 
    GROUP BY 
      task.home
  ) as t2 ON t2.home = address 
ORDER BY 
  profit;
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

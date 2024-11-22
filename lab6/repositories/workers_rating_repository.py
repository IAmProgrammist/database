from lab6.repositories.base import Repository


class WorkersRatingRepository(Repository):
    def __init__(self, connection, dtogenerator):
        super().__init__(connection, "", dtogenerator)

    def select(self, keys: list[str]):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f'''
SELECT 
  worker.inn AS worker_inn, 
  COALESCE (t1.completed, 0) as completed, 
  (
    1.0 * COALESCE (t1.completed, 0) / t2.total
  ) as rating 
FROM 
  worker 
  LEFT JOIN (
    SELECT 
      workers_tasks.worker_inn as worker_inn, 
      COUNT(*) as completed 
    FROM 
      workers_tasks 
      INNER JOIN task ON task.id = workers_tasks.task_id 
    WHERE 
      workers_tasks.worker_inn = worker_inn 
      AND task.completed_date IS NOT NULL 
	  AND task.until_date > '2004-01-01'
	  AND task.until_date < '2040-12-12'
    GROUP BY 
      workers_tasks.worker_inn
  ) t1 ON t1.worker_inn = worker.inn 
  INNER JOIN (
    SELECT 
      workers_tasks.worker_inn as worker_inn, 
      COUNT(*) as total 
    FROM 
      workers_tasks 
      INNER JOIN task ON task.id = workers_tasks.task_id 
    WHERE 
      workers_tasks.worker_inn = worker_inn 
	  AND task.until_date > '2004-01-01'
	  AND task.until_date < '2040-12-12'
	GROUP BY 
      workers_tasks.worker_inn
  ) t2 ON t2.worker_inn = worker.inn 
ORDER BY 
  completed desc;
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


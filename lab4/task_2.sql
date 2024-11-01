SELECT 
  lab_4.worker.inn AS worker_inn, 
  COALESCE (t1.completed, 0) as completed, 
  (
    1.0 * COALESCE (t1.completed, 0) / t2.total
  ) as rating 
FROM 
  lab_4.worker 
  LEFT JOIN (
    SELECT 
      lab_4.workers_tasks.worker_inn as worker_inn, 
      COUNT(*) as completed 
    FROM 
      lab_4.workers_tasks 
      INNER JOIN lab_4.task ON lab_4.task.id = lab_4.workers_tasks.task_id 
    WHERE 
      lab_4.workers_tasks.worker_inn = worker_inn 
      AND lab_4.task.completed_date IS NOT NULL 
    GROUP BY 
      lab_4.workers_tasks.worker_inn
  ) t1 ON t1.worker_inn = lab_4.worker.inn 
  LEFT JOIN (
    SELECT 
      lab_4.workers_tasks.worker_inn as worker_inn, 
      COUNT(*) as total 
    FROM 
      lab_4.workers_tasks 
      INNER JOIN lab_4.task ON lab_4.task.id = lab_4.workers_tasks.task_id 
    WHERE 
      lab_4.workers_tasks.worker_inn = worker_inn 
    GROUP BY 
      lab_4.workers_tasks.worker_inn
  ) t2 ON t2.worker_inn = lab_4.worker.inn 
ORDER BY 
  completed desc;

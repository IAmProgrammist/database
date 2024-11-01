SELECT 
  lab_4.home.address as address, 
  (
    COALESCE(t1.plus, 0) - COALESCE(t2.minus, 0)
  ) as profit 
FROM 
  lab_4.home 
  LEFT JOIN (
    SELECT 
      lab_4.contract.home AS home, 
      SUM(lab_4.payment.payment) as plus 
    FROM 
      lab_4.payment 
      LEFT JOIN lab_4.contract ON lab_4.contract.id = lab_4.payment.contract_id 
    GROUP BY 
      lab_4.contract.home
  ) as t1 ON t1.home = address 
  LEFT JOIN (
    SELECT 
      lab_4.task.home AS home, 
      SUM(lab_4.task.payment) as minus 
    FROM 
      lab_4.task 
    GROUP BY 
      lab_4.task.home
  ) as t2 ON t2.home = address 
ORDER BY 
  profit

SELECT 
  lab_4.resident.snp, 
  SUM(lab_4.payment.payment) AS debt, 
  lab_4.payment.energy_source 
FROM 
  lab_4.resident 
  INNER JOIN lab_4.residents_contracts ON lab_4.residents_contracts.resident_passport_data = lab_4.resident.passport_data 
  INNER JOIN lab_4.contract ON lab_4.residents_contracts.contract_id = lab_4.contract.id 
  INNER JOIN lab_4.payment ON lab_4.payment.contract_id = lab_4.contract.id 
WHERE 
  lab_4.payment.paid_date IS NULL 
GROUP BY 
  lab_4.resident.passport_data, 
  lab_4.payment.energy_source 
ORDER BY 
  debt DESC;

create table residents_contracts(
	resident_passport_data text not null references resident (passport_data) on delete cascade,
	contract_id int not null references contract (id) on delete cascade
)
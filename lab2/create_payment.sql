create table payment(
	id text not null unique primary key,
	paid_date date null,
	until_date date not null,
	contract_id int null references contract (id) on delete set null
)
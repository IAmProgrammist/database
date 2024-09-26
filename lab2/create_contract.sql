create table contract(
id serial not null primary key,
transaction_date date not null,
until_date date not null,
check (until_date > transaction_date),
payment int not null constraint check_contract_payment check (payment >= 0),
home text not null references home (address) on delete restrict
)
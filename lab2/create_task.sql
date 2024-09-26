create table task(
	id serial not null primary key,
	payment int not null check (payment >= 0),
	completed_date date null,
	until_date date not null,
	home text null references home (address) on delete set null
)
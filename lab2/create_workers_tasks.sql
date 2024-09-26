create table workers_tasks(
	worker_inn text not null references worker (inn) on delete cascade,
	task_id int not null references task (id) on delete cascade
)
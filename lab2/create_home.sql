create table home(
address text unique primary key not null,
commisioning date null,
floors int not null constraint floors_check check (floors > 0),
index int not null constraint index_check check (index >= 100000 and index <= 999999)
)
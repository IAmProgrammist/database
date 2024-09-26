create table resident(
passport_data text not null primary key unique,
snp text not null,
email text null,
phone text null
)
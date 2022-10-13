from colazy.wrappers import PgColazy

p = "postgres"

conn = PgColazy(
		dbname=p,
		user=p,
		password=p
	)


@conn.querry_db
def insert_name():
    return ("insert into names (name, lastname) values ('Fred', 'Nit');")


@conn.querry_db
def get_names():
    return ("select * from names;")


insert_name()


names = get_names()

print(names)


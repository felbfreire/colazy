from colazy.wrappers import querry_db


@querry_db
def insert_name():
    return ("insert into names (name, lastname) values ('Fred', 'Nit');")


@querry_db
def get_names():
    return ("select * from names;")



@querry_db
def update_name():
    return ("update names set name = 'John' where id = 1;")


@querry_db
def delete_name():
    return ("delete from names where id = 1;")

from colazy.wrappers import PgColazy 
from colazy.utils import exec_script

import pytest

p = "postgres"

colazy = PgColazy(
		dbname=p,
		user=p,
		password=p
	)

exec_script()


@colazy.query_db
def insert_name():
	return ("insert into names (name, lastname) values ('Fred', 'Nit');")


@colazy.query_db
def get_names():
	return ("select * from names;")


@colazy.query_db
def update_name():
	return ("update names set name =  'John' where id = 1")


@colazy.query_db
def delete_name():
	return ("delete from names  where id = 1")


class TestQuerryes():

	def test_insert_name(self):
		insert_name()

		names = get_names()

		assert names == [(1, 'Fred', 'Nit')]

	def test_update_name(self):
		update_name()
	
		names = get_names()

		assert names == [(1, "John", "Nit")]


	def test_delete_names(self):
		delete_name()

		names = get_names()

		assert names == []

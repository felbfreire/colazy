from .utils import get_cursor, drop_connection

import psycopg2


class PgColazy:

	def __init__(self, **kwargs):
		"""
		Adapter for connectiong postgres database that
		holds udeful methods methods.
		"""

		self.kw = kwargs

		self.dbname = self.kw["dbname"]
		self.user = self.kw["user"]
		self.password = self.kw["password"]


	def get_cursor(self):
		"""Connects to the database then returns a cursor"""

		conn = psycopg2.connect(

			dbname=self.dbname,
			user=self.user,
			password=self.password

		)

		cur = conn.cursor()

		return cur


	def  drop_conn(self, cur):
		"""commits then drops a cursor connection"""

		cur.connection.commit()
		cur.connection.close()
		

	def querry_db(self, fn):
		""" 
		wrapps a querry:

		-> connects to db and create a cursor,
		-> executes a querry (function to be decorated),
		-> then commits and close connection.
		"""

		def wrapper(*args, **kwargs):

			cur = self.get_cursor()

			try:
				to_exec = fn()
			except TypeError:
				print("Function must return a valid querry")

			try:
				cur.execute(to_exec)
			except (psycopg2.Error, TypeError):
				print("Function must return a valid querry")

			try:
				result = cur.fetchall()
				self.drop_conn(cur)
			except psycopg2.Error:
				self.drop_conn(cur)
				return None

			return result

		return wrapper

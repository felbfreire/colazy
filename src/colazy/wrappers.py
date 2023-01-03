import psycopg2


class PgColazy:

	def __init__(self, **kwargs):
		"""
		Adapter for connectiong postgres database that
		holds udeful methods methods.
		"""

		self.kw = kwargs
		self.config = {}

		try:
			self.dbname = self.kw["dbname"]
			self.user = self.kw["user"]
			self.password = self.kw["password"]
		except KeyError:
			print("PgColazy need dbname, user and password information to work")


	def get_cursor(self):
		"""Connects to the database then returns a cursor"""

		if "dbname" and "user" and "password" in self.kw:

			conn = psycopg2.connect(

				dbname=self.dbname,
				user=self.user,
				password=self.password

			)

		elif "dbname" and "user" and "password" in self.config:

			conn = psycopg2.connect(

				dbname=self.config["dbname"],
				user=self.config["user"],
				password=self.config["password"]

			)

		try:
			cur = conn.cursor()
			return cur
		except UnboundLocalError:
			print("PgColazy could't stablish a connection.")


	def  drop_conn(self, cur):
		"""commits then drops a cursor connection"""

		cur.connection.commit()
		cur.connection.close()
		

	def query_db(self, fn):
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
			except TypeError :
				print("Function must return a valid query.")

			try:

				cur.execute(to_exec)
			except (psycopg2.Error, TypeError):
				pass

			try:
				result = cur.fetchall()
				self.drop_conn(cur)
			except psycopg2.Error:
				self.drop_conn(cur)
				return None

			return result

		return wrapper


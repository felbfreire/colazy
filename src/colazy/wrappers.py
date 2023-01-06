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
        try:
            cur.connection.commit()
            cur.connection.close()
        except AttributeError:
            pass


    def query_db(self, fn):
        """ 
        wrapps a querry:

        -> connects to db and create a cursor,
        -> executes a querry (function to be decorated),
        -> then commits and close connection.
        """

        def wrapper(*args, **kwargs):

            cur = self.get_cursor()

            to_exec = fn()
            try:
                cur.execute(to_exec)
            except (psycopg2.Error, AttributeError) as e:
                print(f"Execution error")
            try:
                result = cur.fetchall()
                return result
            except (psycopg2.Error, AttributeError):
                self.drop_conn(cur)

                return None

        return wrapper


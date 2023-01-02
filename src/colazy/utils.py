from .config import db_config as conf

import psycopg2


def get_cursor():
    """ connects to database then returns a cursor """ 
    conn = psycopg2.connect(
            dbname=conf["db_name"],
            password=conf["password"], 
            user=conf["db_user"]
            )

    cur = conn.cursor()

    return cur


def drop_connection(cursor):
    """ commits then drops a connection """

    if isinstance(cursor, psycopg2.extensions.cursor):
        cursor.connection.commit()
        cursor.connection.close()


def exec_script(script: str):
    """ executes a script """

    if isinstance(script, str):
        try:
            with open(script) as file:
                cur = get_cursor()
                cur.execute(file.read())
                drop_connection(cur)
        except FileNotFoundError:
            print("File does not exist.")
    else:
        print(f"exec_script expects a string, found {type(script)}")


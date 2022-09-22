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

    cursor.connection.commit()
    cursor.connection.close()


def exec_script():
    with open("schema.sql") as file:
        cur = get_cursor()
        cur.execute(file.read())

        drop_connection(cur)


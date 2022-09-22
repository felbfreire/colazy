from .utils import get_cursor, drop_connection

import psycopg2


def querry_db(fn):
    """ 
        wrapps a querry:

        -> connects to db and create a cursor,
        -> executes a querry,
        -> then commits and close connection.
    """

    def wrapper(*args, **kwargs):

        cur = get_cursor()

        try:
            to_exec = fn()
        except TypeError:
            print("function must return a valid querry")

        try:
            cur.execute(to_exec)
        except (psycopg2.Error, TypeError):
            print("Function must return a valid querry")

        try:
            result = cur.fetchall()
            cur.connection.close()
        except psycopg2.Error: 
            drop_connection(cur)
            return None

        return result

    return wrapper


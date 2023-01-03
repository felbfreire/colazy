Colazy is a package that contains utils for postgres database. Its main
object is PgColazy, which connect, commit and close with a single method. So we
do not need to manage connections.

Fisrt we need to instatiate an PgColazy object, passing configuration data about the
connection. Use the querry_db method as a decorator, that decorates a function which returns a querry.


```bash
from colazy import PgColazy

p = "postgres"

conn = PgColazy(dbname=p, user=p, password=p)
```

you can also instantiate PgColazy passng nothing: PgColazy(),
and then use the instance variable config:

```bash
conn.config["dbname"] = p
conn.config["user"] = p
conn.config["password"] = p
```

```bash
@conn.query_db
def get_names():
	return ("select * from names;")

get_names()
```
if you have postgres database, and table names, it
should output something.


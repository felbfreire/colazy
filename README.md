Colazy is a package that contains utils for postgres database. Its main
decorator is @querry_db, wich connect, commit and close in a single decorator. So we
do not need to manage connections.


```bash
from colazy.wrappers import querry_db


@querry_db
def get_names():
	return ("select * from names;")

get_names()
```
if you have postgres database, and table names, it
should output something.


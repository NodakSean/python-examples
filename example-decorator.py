"""
Sean Johnson
Python  3.5
Create and use a decorator that checks for an existing database connection.
If no connection, create one and pass the connection info to the
execute_query() function.
"""

class Database():
    """Stub a database connection."""
    def __init__(self):
        self.db = "biz"
        self.cursor = "baz"

    def establish_connection(self):
        print("Fetching DB connection")
        return self.db, self.cursor


def dbconnection(function):
    """Return a database connection, as named parameter, to the decorated function."""
    def wrapper(*args, **kwargs):
        if "db_args" not in kwargs:
            db, cursor = Database().establish_connection()
            kwargs["db_args"] = db, cursor
        return function(*args, **kwargs)
    return wrapper

@dbconnection
def execute_query(connection=None, schema=None, db_args=None):
    print("Executing query with DB connection: {}".format(db_args))


print()
print("Executing Query")
execute_query(db_args=("foo", "bar"))
print("All Done!")
print()
print("Executing Query")
execute_query()
print("All Done!")
print()

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
        self.connection = "baz"

    def establish_connection(self):
        print("Fetching DB connection")
        return self.connection


def dbconnection(function):
    """Return a database connection, as named parameter, to the decorated function."""
    def wrapper(*args, **kwargs):
        if "connection" not in kwargs:
            connection = Database().establish_connection()
            kwargs["connection"] = connection
        return function(*args, **kwargs)
    return wrapper


@dbconnection
def execute_query(connection=None):
    print("Executing query with DB connection: {}".format(connection))


print()
print("Executing Query")
execute_query(connection="foo")
print("All Done!")
print()
print("Executing Query")
execute_query()
print("All Done!")
print()

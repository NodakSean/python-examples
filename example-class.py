"""
A Trivial Python Class Example.
Python 3.5
"""


class Employee:
    """A trivial class example."""

    _number_of_employees = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = 0
        Employee._number_of_employees += 1

    @property
    def email_address(self):
        return "{}.{}@domain.com".format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @staticmethod
    def compare(employee_1, employee_2):
            return employee_1.employee_id > employee_2.employee_id

    @property
    def employee_count(self):
        return Employee._number_of_employees

    def __str__(self):
        return "Name:{} | Email: {} | ID: {}".format(self.fullname, self.email_address, self.employee_id)

    def __repr__(self):
        return "Employee({}, {})".format(self.first_name, self.last_name)

print()
a = Employee("John", "Smith")
a.employee_id = 21
print("Employee Count: {}".format(a.employee_count))
print(a)
print(repr(a))

print()

b = Employee("Mike", "Gordon")
b.employee_id = 42
print("Employee Count: {}".format(b.employee_count))
print(b)
print(repr(b))

print()

print("{} > {}: {}".format(a.employee_id, b.employee_id, a.compare(a, b)))






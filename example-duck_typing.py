"""
Sean Johnson
Python 3.5
The canonical example of duck typing.
"""


class Duck:

    @staticmethod
    def quack():
        print("Quack, quack!")

    @staticmethod
    def fly():
        print("Flap, Flap!")

class Person:

    @staticmethod
    def quack():
        print("I'm Quackin'!")

    @staticmethod
    def fly():
        print("I'm Flyin'!")


def in_the_forest(mallard):
    mallard.quack()
    mallard.fly()


in_the_forest(Duck())
print()
in_the_forest(Person())

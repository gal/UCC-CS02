class Person:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary


dave = Person("Dave", "32", 55000)
print(dave._name, dave._salary)
# output: Dave 55000

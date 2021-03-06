#!/usr/bin/env python3
"""
- Write a class representing an employee.
- Every employee should have: name, surname and salary.

e1 = Employee(...)
e1.name_set("Jan")
e1.surname_set("Kowalski")
e1.salary_set(5000)
also something that will allow representing object as string
"""

class Employee:
    """This is a class representing a single employee."""
    def __init__(self, name, surname, salary):
        self.name_set(name)
        self.surname_set(surname)
        self.salary_set(salary)
    def name_set(self, name):
        """Set the (first) name of an employee."""
        self.name = name
    def surname_set(self, surname):
        """Set the (last) name of an employee."""
        self.surname = surname
    def salary_set(self, salary):
        """Set the salary of an employee."""
        if salary < 2000:
            # Throw exception ;p
            print("Nope")
        else:
            self.salary = salary
    def __str__(self):
        """Return string representation of an employee (name and salary)."""
        return self.name + " " + self.surname + " zarabia " + str(self.salary)

e1 = Employee("Arkadiusz", "Testowski", 10000)
print(e1)


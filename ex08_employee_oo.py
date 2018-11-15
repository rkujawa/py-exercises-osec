#!/usr/bin/env python3
"""
- Write a class representing an employee.
- Every employee should have: name, surname and salary.

e1 = Employee()
e1.name_set("Jan")
e1.surname_set("Kowalski")
e1.salary_set(5000)
also something that will allow representing object as string
"""

class Employee:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.salary = 0
    def name_set(self, name):
        self.name = name
    def surname_set(self, surname):
        self.surname = surname
    def salary_set(self, salary):
        if salary < 2000:
            # Throw exception ;p
            print("Nope")
        else:
            self.salary = salary
    def __str__(self):
        return self.name + " " + self.surname + " zarabia " + str(self.salary)

e1 = Employee()
e1.name_set("Arkadiusz")
e1.surname_set("Testowski")
e1.salary_set(10000)
print(e1)


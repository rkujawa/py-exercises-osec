#!/usr/bin/env python3
"""
- Create a database (dict) of employees, where surname is used as key, and value is holding a tuple
with position and salary.
- Allow the user to specify 3 things (surname, position, salary) and add it to database.
- Allow listing employeed and searching for employee by surname
"""
from snack import *

e1 = ("programista", 1000)
e2 = ("architekt", 3000)

employees = { } 

employees["kowalski"] = e1
employees["testowski"] = e2

#print(employees)

def employees_add():
    screen = SnackScreen()
    eres = EntryWindow(screen, 'Add new employee', 'Input data below',
                       ['Surname', 'Position', 'Salary'])

    screen.finish()
    if eres[0] == 'ok':
        new_employee = (eres[1][1], eres[1][2])
        employees[eres[1][0]] = new_employee
#    print(eres)
#    print(new_employee)

def employees_find():
    screen = SnackScreen()
    eres = EntryWindow(screen, 'Find employee', 'Input data below', ['Surname'])
    screen.finish()

    if eres[0] == 'ok':
        if eres[1][0] in employees.keys():
            screen = SnackScreen()
            g = GridForm(screen, "Employee info", 1, 4)
            e = employees[eres[1][0]]
            etext = e[0] + " " + str(e[1])
            ti = Textbox(height = 10, width = 20, text = etext)
            cb = Button("Ok")
            g.add(ti, 0, 0)
            g.add(cb, 0, 1, growx = 1)
            results = g.runOnce()  
            screen.finish()



def employees_list():
    screen = SnackScreen()
    li = Listbox(height = 10, width = 40, returnExit = 1)
    for i in employees.keys():
        li.append(i, 1)

    g = GridForm(screen, "list", 1, 4)
    bb = ButtonBar(screen, (("Add", "add"), ("Find", "find"), ("Exit", "exit")))
    g.add(li, 0, 0)
    g.add(bb, 0, 3, growx = 1)

    result = g.runOnce()
    screen.finish()
    fn = bb.buttonPressed(result)

    return fn


fn = "" 
while True:
    fn = employees_list()

    if fn == "add":
        employees_add()
    elif fn == "find":
        employees_find()
    elif fn == "exit":
        break

print(employees)


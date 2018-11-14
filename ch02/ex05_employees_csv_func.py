#!/usr/bin/python3
"""
- Read dane.txt and built python data structures representing it (use split())
- Print out all employees from database
- Increase all employees salary by 10%
#- All programmers should additional have salaries increased by 500
- Write out the modified database to nowe_dane.txt file in the same format (use join())
- Use functions where appropriate
"""
import csv

def employees_read(filename):
    emp = []
    with open(filename) as csvf_read:
        reader = csv.reader(csvf_read)
        for rrow in reader:
            emp.append(rrow)
    return emp

def employees_salary_increase(emp, inc):
    for e in emp:
        e[2] = int(e[2])
        e[2] += e[2] * inc 
#        if e[1] == "programista":
#            e[2] += 500

def employees_write(filename, emp):
    with open(filename, 'w') as csvf_write:
        writer = csv.writer(csvf_write)
        for e in emp:
            writer.writerow(e)

def employees_print(emp):
    print(emp)

employees = employees_read('dane.txt')
employees_salary_increase(employees, 0.1)
employees_print(employees)
employees_write('nowe_dane.txt', employees)

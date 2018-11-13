#!/usr/bin/python3
"""
- Read dane.txt and built python data structures representing it (use split())
- Print out all employees from database
- Increase all employees salary by 10%
- All programmers should additional have salaries increased by 500
- Write out the modified database to nowe_dane.txt file in the same format (use join())
"""
import csv

csvf_read = open('dane.txt')
reader = csv.reader(csvf_read)

employees = []

for rrow in reader:
    employees.append(rrow)

print(employees)

for e in employees:
    e[2] = int(e[2])
    e[2] += e[2] * 0.1
    if e[1] == "programista":
        e[2] += 500

print(employees)

csvf_write = open('nowe_dane.txt', 'w')
writer = csv.writer(csvf_write)

for e in employees:
    writer.writerow(e)

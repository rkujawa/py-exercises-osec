#!/usr/bin/env python3
"""Write a program to collect lunch orders from users
- Predefine a list of lunches
- Print the amount of ordered lunches
- Allow appending new lunches to list
- Print the newly define lunch using indexing
"""

import argparse

OFILE = open('orders.txt', 'r+')

orders = []
for t in OFILE:
    orders.append(t.strip().split(":"))

for t in orders:
    t[1] = int(t[1])

PARSER = argparse.ArgumentParser()
PARSER.add_argument('-l', action='store_true', help="list ordered lunches")
PARSER.add_argument('-a', action='store', help="add a new lunch")
PARSER.add_argument('-o', action='store', help="order a lunch")
ARGS = PARSER.parse_args()
print(ARGS)

if ARGS.a:
    orders.append([ARGS.a, 0])
    for t in orders:
        line = t[0] + ':' + str(t[1])
    OFILE.write(line + '\n')

if ARGS.o:
    if ARGS.o in list(map(lambda x: x[0], orders)):
        print("taki obiad jest na liscie")
    else:
        print("no such lunch on the order list, please add it first")

    for t in orders:
        if t[0] == ARGS.o:
            t[1] += 1

    print(orders)

    OFILE.close()
    OFILE = open('orders.txt', 'w')
    for t in orders:
        line = t[0] + ':' + str(t[1])
        OFILE.write(line + '\n')

if ARGS.l:
    for i in orders:
        print(i)

OFILE.close()

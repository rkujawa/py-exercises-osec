#!/usr/bin/env python3

from order import *
import csv

class OrderCSV(Order):

    def save(self, filename):
        with open(filename, 'w') as csvfh:
            writer = csv.writer(csvfh)
            for i in self:
                writer.writerow(i.to_list())


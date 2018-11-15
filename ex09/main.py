#!/usr/bin/env python3

from dish import *
from order import *
from order_csv import *

o = OrderCSV()
o.dish_add(Dish("kebs", "zenon", "na cienkim"))
o.dish_add(Dish("makaron", "tester", "z kiełbasą"))
o.save('luncheslol.txt')
o.printit()


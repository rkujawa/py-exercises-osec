#!/usr/bin/env python3

from dish import *
from order import *

o = Order()
o.dish_add(Dish("kebs", "zenon", "na cienkim"))
o.dish_add(Dish("makaron", "tester", "z kiełbasą"))
o.printit()


#!/usr/bin/env python3

class Order(list):

    def dish_add(self, dish):
        self.append(dish)

    def printit(self):
        print(self.__str__())

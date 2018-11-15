#!/usr/bin/env python3

class Dish:
    def __init__(self, name, owner, comment=None):
        self.name = name
        self.owner = owner
        if comment != None:
            self.comment = comment

    def __str__(self):
        return self.name + " for " + self.owner

    def __repr__(self):
        return self.__str__()

    def to_list(self):
        return [self.name, self.owner, self.comment]
 

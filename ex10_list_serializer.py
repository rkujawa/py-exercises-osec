#!/usr/bin/env python3
"""
Write a module that will serialize/deserialize list of strings.
i.e.

import list_serializer
list_serializer.serialize(['a','b','c'], 'listery.txt')
list_serializer.deserialize('litery.txt') # => ['a', 'b', 'c']

Mozliwe bledy:
1) NonexistentFileError -- jeśli deserializowany plik nie isstnieje
2) InvalidDataError --  Jesli lista zawiera nie tylko str
3) InsufficientPermissionsError -- Jeśli brak uprawnień

Przerób wszystkie wyjątki aby były pochodne od ListSerializerError.

"""
import csv

class ListSerializerError(Exception):
    pass

class NonexistentFileError(ListSerializerError):
    pass

class InvalidDataError(ListSerializerError):
    pass

class InsufficientPermissionsError(ListSerializerError):
    pass

def serialize(l, filename):
    for elem in l:
        if type(elem) != str:
            raise InvalidDataError()
 
    try:
        with open(filename, 'w') as fh:
            writer = csv.writer(fh)
            writer.writerow(l)
    except PermissionError as e:
        raise InsufficientPermissionsError(e)

def deserialize(filename):
    l = []
    try:
        with open(filename) as fh:
            reader = csv.reader(fh)
            #for rrow in reader:
            l.append(reader.__next__())
    except PermissionError as e:
        raise InsufficientPermissionsError(e)
    except FileNotFoundError as e:
        raise NonexistentFileError(e)

    return l

def test_it():
    testfile = "listtest.txt"
    l_bad = ["aaa", 123, "ccc"]
    l_good = ["aaa", "bbb", "ccc"]
    l_read = []

    try:
        serialize(l_bad, testfile)
    except InvalidDataError as e:
        print("InvalidDataError caught as expected.")
    
    try:
        serialize(l_good, testfile)
    except ListSerializerError:
        print("Other ListSerializerError happened!")

    try:    
        l_read = deserialize(testfile)
    except ListSerializerError as e:
        print("Some ListSerializerError happened: " + str(type(e)))

    if l_read == l_good:
        print("All is well")

if __name__ == "__main__":
    test_it() 



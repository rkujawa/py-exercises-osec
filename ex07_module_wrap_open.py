#!/usr/bin/env python3
"""Exercise text:
- Create a module containing functions: file_load() and file_save(), like:
- contents = file_load('filename.txt')
- file_save('filename.txt', contents)
- contents should be a list of lines in file, without newline characters
- Write tests for this module, which will execute only when module is ran as program
- Write docstrings for module and function (should be readably with pydoc).
"""

def file_load(filename):
    """Load a file.

    Argument `filename` contains a path to file to load.

    Returns a list of lines in the file, without newline characters.
    """
    contents = []
    with open(filename) as file_rd:
        for l in file_rd:
            contents.append(l.strip())
    return contents

def file_save(filename, contents):
    """Save a file.

    Argument `filename` contains a path to file to be saved (overwritte if exist).

    Does not return anything.
    """
    with open(filename, 'w') as file_wr:
        for l in contents:
            file_wr.write(l + '\n')

if __name__ == "__main__":
    testlines = file_load('test.txt')
    print(testlines)
    file_save('test2.txt', testlines)


#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry
11;rgb:0000/0000/0000
bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

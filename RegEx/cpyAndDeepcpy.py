#!/usr/bin/python3
# coding=utf-8


import copy

a1 = 123123
b1 = copy.copy(a1)
print(id(a1))
print(id(b1))

print("-"*10)
a2 = "abc"
b2 = copy.copy(a2)

print(id(a2))
print(id(b2))

print("-"*10)
a3 = (1, 2, ["hello", "world"])
b3 = copy.copy(a3)

print(id(a3))
print(id(b3))

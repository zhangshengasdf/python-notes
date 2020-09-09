#!/usr/bin/python3
# coding=utf-8


class Person(object):
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        if new_age >= 150:
            print("成精了")
        else:
            self.__age = new_age

class Person1(object):
    def __int__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 150:
            print("成精了")
        else:
            self.__age = new_age
    age = property(get_age, set_age)
    
p = Person1()
p.age = 100
print(p.age)
p.age = 150

#!/usr/bin/python3
# coding=utf-8


import time

def get_time(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print("函数执行花费了%f" % (end - begin))
    return inner

@get_time
def func1():
    for i in range(100000):
        print(i)


func1()

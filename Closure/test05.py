#!/usr/bin/python3
# coding=utf-8


def logging(fn):
    def inner(*args, **kwargs):
        print("--正在计算中--")
        fn(*args, **kwargs)
        
    return inner

@logging
def sum_num(*args, **kwargs):
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result += value

    print(result)
    
    
sum_num(1,2, a = 3)
#print(result)

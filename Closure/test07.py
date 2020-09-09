#!/usr/bin/python3
# coding=utf-8


def logging(flag):
    def decorator(fn):
        def inner(num1, num2):
            if flag == '+':
                print("--正在加法运算--")
            elif flag == '-':
                print("--正在减法运算--")
            result = fn(num1, num2)

            return result
        return inner

    return decorator

@logging('+')
def add(a, b):
    result = a + b
    return result

@logging('-')
def sub(a, b):
    result = a - b
    return result


result = sub(1, 2)
print(result)

print(add(1,2))

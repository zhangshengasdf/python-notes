#!/usr/bin/python3
# coding=utf-8


def mygenerater(n):
    for i in range(n):
        print('开始...')
        yield i*2
        print('完成一次...')

def fibonacci(num):
    a = 0
    b = 1
    current_index = 0
    while current_index < num:
        result = a
        a, b = b, a+b
        current_index += 1
        yield result


if __name__ == '__main__':
    fib = fibonacci(50)
    for value in fib:
        print(value)



#!/usr/bin/python3
# coding=utf-8


def func_out(num1):
    def func_in(num2):
        result = num1 + num2
        print('结果是：', result)
    return func_in


if __name__ == '__main__':
    f = func_out(1)
    f(2)
    f(3)


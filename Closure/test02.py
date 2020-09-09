#!/usr/bin/python3
# coding=utf-8


def func_out(num1):

    def func_in(num2):
        nonlocal num1
        num1 = 10
        result = num1 + num2
        print('result:', result)

    print(num1)
    func_in(1)
    print(num1)

    return func_in

func_out(1)(2)



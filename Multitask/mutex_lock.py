#!/usr/bin/python3
# coding=utf-8


import threading


g_num = 0

g_lock = threading.Lock()

def sum_num1():
    g_lock.acquire()

    for i in range(1000000):
        global g_num

        g_num += 1
    print("sum1:", g_num)

    g_lock.release()

def sum_num2():
    g_lock.acquire()

    for i in range(1000000):
        global g_num

        g_num += 1
    print("sum2:", g_num)

    g_lock.release()

if __name__ == '__main__':

    first_thread = threading.Thread(target = sum_num1)
    second_thread = threading.Thread(target = sum_num2)

    first_thread.start()
    second_thread.start()


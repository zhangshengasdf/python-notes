#!/usr/bin/python3
# coding=utf-8


import multiprocessing
import time

def task(count):
    for i in range(count):
        print("working...")
        time.sleep(0.2)
    else:
        print("well-done!")

def task1(count):
    for i in range(count):
        print("working...")
        time.sleep(0.2)
    else:
        print("well-done!")


if __name__ == '__main__':
    sub_process = multiprocessing.Process(target = task, args = (5,))
    sub_process1 = multiprocessing.Process(target = task, kwargs = {"count": 5})

    sub_process.start()
    sub_process1.start()

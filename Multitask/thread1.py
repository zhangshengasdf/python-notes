#!/usr/bin/python3
# coding=utf-8


import threading
import time


def task(count):
    for i in range(count):
        print("task working...")
        time.sleep(0.2)
    else:
        print("task well-done!")

def task1(count):
    for i in range(count):
        print("task1 working...")
        time.sleep(0.2)
    else:
        print("task1 well-done!")

if __name__ == '__main__':
    sub_thread = threading.Thread(target = task, args = (5,))
    sub_thread1 = threading.Thread(target = task1, kwargs = {"count": 5})

    sub_thread.start()
    sub_thread1.start()



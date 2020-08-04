#!/usr/bin/python3
# coding=utf-8


import multiprocessing
import time
import os

def dance():
    print("dance:", os.getpid())
    print('dance:', multiprocessing.current_process())
    print("dance的父进程编号:", os.getppid())
    for i in range(5):
        print("dancing...")
        time.sleep(0.2)
        os.kill(os.getpid(), 9)

def sing():
    print("sing:", os.getpid())
    print('sing:', multiprocessing.current_process())
    print("sing的父进程编号:", os.getppid())
    for i in range(5):
        print("singing...")
        time.sleep(0.2)


if __name__ == '__main__':

    print("main:", os.getpid())
    print("main:", multiprocessing.current_process())
    dance_process = multiprocessing.Process(target = dance)
    sing_process = multiprocessing.Process(target = sing)

    dance_process.start()
    sing_process.start()

#!/usr/bin/python3
# coding=utf-8


import threading
import time

def sing():
    for i in range(3):
        print("singing...%d" % i)
        time.sleep(1)

def dance():
    for i in range(3):
        print("dancing...%d" % i)
        time.sleep(1)

if __name__ == '__main__':
    
    sing_thread = threading.Thread(target = sing)
    dance_thread = threading.Thread(target = dance)

    sing_thread.start()
    dance_thread.start()


#!/usr/bin/python3

from threading import Thread, Semaphore, Lock
import time
from random import randint
import sys


class MyThread(Thread):
    #semaphore = Semaphore(1)
    mutex = Lock()

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        self.calc_random(5)

    def calc_random(self, values):
        a = []
        b = []
        c = []
        for i in range(0,values):
            a.append(randint(0,9))
            b.append(randint(0,9))
            c.append(a[i] + b[i])

            time.sleep(0.5)

            sys.stderr.write(self.name + ": " + str(a[i]) +
                             " + " + str(b[i]) + " = "
                             + str(c[i]) + "\n")
            i += 1
        """
        with MyThread.semaphore:
            print("Hello my Name is: " + self.name)

            for i in range(0,values):
                print(self.name + ":c[" + str(i) + "]=" + str(c[i]))"""
        MyThread.mutex.acquire()
        try:
            print("Hello my Name is: " + self.name)

            for i in range(0, values):
                print(self.name + ":c[" + str(i) + "]=" + str(c[i]))
        finally:
            MyThread.mutex.release()



threads = []
for i in range(1,11):
    threads.append(MyThread("Thread-" + str(i)))

for mythread in threads:
    mythread.start()
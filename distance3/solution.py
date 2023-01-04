#!/usr/bin/python3
""" This module is for the distance learning 3 tasks. """

from math import floor
import subprocess
from threading import Thread
from threading import Semaphore


def read_file(filename):
    """ Reads the lines from input file and returns them in a list. """
    numbers = []
    f_obj = open(filename, "r")
    for line in f_obj.readlines():
        numbers.append(line)
    return numbers


def calc(value):
    """ Uses the calc.sh script to calculate the new line value. """
    returnvalue = int(subprocess.check_output(["./calc.sh", value]))
    return returnvalue


def slowsort_start(arr, i, j, semaphore):
    """ Doubles the line numbers and sorts it afterwards with slowsort. """
    with semaphore:
        for idx, number in enumerate(arr):
            arr[idx] = calc(number)
        slowsort(arr, i, j)


def slowsort(arr, i, j):
    """ Sorts the list using the slowsort algorithm. """
    if i >= j:
        return
    mid = floor((i+j)/2)
    slowsort(arr, i, mid)
    slowsort(arr, mid+1, j)

    if arr[j] < arr[mid]:
        temp = arr[j]
        arr[j] = arr[mid]
        arr[mid] = temp

    slowsort(arr, i, j-1)


def write_numbers(filename, numbers):
    """ Writes the numbers into the specified file and sets the permissions. """
    f_obj = open(filename, "w")
    content = ""
    for number in numbers:
        content += str(number) + "\n"
    f_obj.write(content[0:-1])
    subprocess.call(["chmod", "600", filename])


NUM1 = read_file("1-100.csv")
NUM2 = read_file("101-200.csv")
NUM3 = read_file("201-300.csv")
NUM4 = read_file("301-400.csv")
NUM5 = read_file("401-500.csv")
NUM6 = read_file("501-600.csv")

SEMAPHORE = Semaphore(2)

THREAD1 = Thread(target=slowsort_start, args=(NUM1, 0, 99, SEMAPHORE))
THREAD2 = Thread(target=slowsort_start, args=(NUM2, 0, 99, SEMAPHORE))
THREAD3 = Thread(target=slowsort_start, args=(NUM3, 0, 99, SEMAPHORE))
THREAD4 = Thread(target=slowsort_start, args=(NUM4, 0, 99, SEMAPHORE))
THREAD5 = Thread(target=slowsort_start, args=(NUM5, 0, 99, SEMAPHORE))
THREAD6 = Thread(target=slowsort_start, args=(NUM6, 0, 99, SEMAPHORE))

THREAD1.start()
THREAD2.start()
THREAD3.start()
THREAD4.start()
THREAD5.start()
THREAD6.start()

THREAD1.join()
THREAD2.join()
THREAD3.join()
THREAD4.join()
THREAD5.join()
THREAD6.join()

write_numbers("2-200.csv", NUM1)
write_numbers("202-400.csv", NUM2)
write_numbers("402-600.csv", NUM3)
write_numbers("602-800.csv", NUM4)
write_numbers("802-1000.csv", NUM5)
write_numbers("1002-1200.csv", NUM6)
#!/usr/bin/python3
from math import floor


def readFile(filename):
    numbers = []
    f_obj = open(filename, "r")
    for line in f_obj.readlines():
        numbers.append(int(line))
    return numbers


def calc(value):
    returnvalue = exec("./calc.sh " + value)
    return returnvalue


def slowsort_start(arr, i, j):
    for k in range(0, len(arr)):
        arr[k] = calc(arr[k])
    slowsort(arr, i, j)


def slowsort(A, i, j):
    if i >= j:
        return
    m = floor((i+j)/2)
    slowsort(A, i, m)
    slowsort(A, m+1, j)

    if A[j] < A[m]:
        h = A[j]
        A[j] = A[m]
        A[m] = h

    slowsort(A, i, j-1)


def writeNumbers(filename, numbers):
    f_obj = open(filename, "w")
    s = ""
    for number in numbers:
        s += str(number) + "\n"
    f_obj.write(s[0:-1])


num1 = readFile("1-100.csv")
num2 = readFile("101-200.csv")
num3 = readFile("201-300.csv")
num4 = readFile("301-400.csv")
num5 = readFile("401-500.csv")
num6 = readFile("501-600.csv")

for i in range(0, 100):
    num1[i] = calc(num1[i])
    num2[i] = calc(num2[i])
    num3[i] = calc(num3[i])
    num4[i] = calc(num4[i])
    num5[i] = calc(num5[i])
    num6[i] = calc(num6[i])

slowsort_start(num1, 0, 99)
slowsort_start(num2, 0, 99)
slowsort_start(num3, 0, 99)
slowsort_start(num4, 0, 99)
slowsort_start(num5, 0, 99)
slowsort_start(num6, 0, 99)

writeNumbers("21-2100.csv", num1)
writeNumbers("2101-2200.csv", num2)
writeNumbers("2201-2300.csv", num3)
writeNumbers("2301-2400.csv", num4)
writeNumbers("2401-2500.csv", num5)
writeNumbers("2501-2600.csv", num6)
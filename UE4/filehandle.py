import time
from datetime import datetime


def writeToFile(filename):
    for i in range(0,26):
        timestamp = "Write Line: " + str(i) + " " + str(datetime.fromtimestamp(time.time()))
        print(timestamp)
        with open(filename, "w") as f_obj:
            f_obj.write(timestamp)
        time.sleep(1)


def appendToFile(filename):
    for i in range(0,26):
        timestamp = "Append Line: " + str(i) + " " + str(datetime.fromtimestamp(time.time()))
        print(timestamp)
        with open(filename, "a") as f_obj:
            f_obj.write(timestamp + "\n")
        time.sleep(1)


def readFromFile(filename):
    with open(filename) as f:
        lines = f.readlines()

    num_lines = len(lines)
    for i in range(0,num_lines):
        print(lines[i])
        time.sleep(1)


writeToFile("file1.txt")
appendToFile("file2.txt")
readFromFile("file1.txt")
readFromFile("file2.txt")
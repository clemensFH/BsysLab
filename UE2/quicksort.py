import time


def quicksort(arr, idxl, idxr):
    if idxl < idxr:
        pivot = part(arr, idxl, idxr)
        quicksort(a, idxl, pivot)
        quicksort(a, pivot+1, idxr)


def part(arr, idxl, idxr):
    pivot = arr[idxl]
    border = idxl

    for i in range(idxl+1, idxr):
        if a[i] < pivot:
            a[i], a[border] = a[border], a[i]
            border += 1

    pivot, a[border] = a[border], pivot
    return border


a = [i for i in range(599, -1, -1)]
print("Before sort:\n" + str(a))
start_time = time.time()
quicksort(a, 0, 600)
t = (time.time() - start_time)
print("After sort:\n" + str(a))
print("Time needed: " + str(t) + " seconds")
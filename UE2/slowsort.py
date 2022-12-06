from math import floor


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


arr = [i for i in range(149, -1, -1)]
slowsort(arr, 0, 149)
print(arr)
from math import floor
from operator import ge, lt

l = [16, 23, 3, 4, 66, 123, 2, 1, 65, 999]


def subList(L, op, pivot):
    return [*filter(lambda num: op(num, pivot), L)]


def quickSort(L):
    if len(L) <= 1:
        return L
    pivot = L[floor(len(L) / 2) - 1]
    t = L[0:floor(len(L) / 2) - 1] + L[floor(len(L) / 2):]
    return quickSort(subList(t, lt, pivot)) + [pivot] + quickSort(subList(t, ge, pivot))


print(quickSort(l))

from random import seed
from random import random
from math import floor
import time


def generateNumbers(n):
    seed(floor(time.time()))
    l = [floor(random() * 100) + 1 for i in range(n)]
    l.sort()
    return l


def avg(l):
    return sum(l) / len(l)


def findSecondMax(l):
    l1 = l.copy()
    M1 = max(l1)
    l1.remove(M1)
    return max(l1)


def findSecondMin(l):
    l1 = l.copy()
    M1 = min(l1)
    l1.remove(M1)
    return min(l1)


def findEven(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result.append(x)
    return len(result)


def program(n):
    l = generateNumbers(20)
    average = avg(l)
    m = min(l)
    M = max(l)
    M2 = findSecondMax(l)
    m2 = findSecondMin(l)
    ev = findEven(l)
    print(l)
    print('Avg=', average)
    print('Min=', m, ', Max', M)
    print('Min2=', m2, ', Max2=', M2)
    print('#Even=', ev)


program(20)

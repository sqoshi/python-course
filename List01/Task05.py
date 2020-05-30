from math import floor


def frac(n):
    if n == 1:
        return 1
    else:
        return n * frac(n - 1)


def fraczero(n):
    x = frac(n)
    print(x)
    counter = 0
    while x % 10 == 0:
        counter += 1
        x = x // 10
    return counter


fraczero(99998150012677960509854672544694223)

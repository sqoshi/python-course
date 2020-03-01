from math import floor


def frac(n):
    if n == 1:
        return 1
    else:
        return n * frac(n - 1)


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


def fraczero(n):
    print(floor(sum(n) / 10), frac(n))


fraczero(24)

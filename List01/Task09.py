from cmath import sin
import re


def ret(s):
    s = str(s)

    if s.isdigit():
        return float(s)
    for c in ('-', '+', '*', '/', '^'):
        left, op, right = s.partition(c)
        if op == '*':
            return ret(left) * ret(right)
        elif op == '/':
            return ret(left) / ret(right)
        elif op == '+':
            return ret(left) + ret(right)
        elif op == '-':
            return ret(left) - ret(right)
        elif op == '^':
            return ret(left) ** ret(right)


def func(x):
    return sin(x)


print(ret('4*3+2*6^2'))

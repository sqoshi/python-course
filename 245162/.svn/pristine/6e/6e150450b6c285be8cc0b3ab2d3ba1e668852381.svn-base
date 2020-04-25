import sys
import time


def measureExecution(func):
    def wrapper():
        start = time.process_time()
        func()
        return time.process_time() - start

    return wrapper


@measureExecution
def multiplyby2():
    x = 1.0
    while x < sys.maxsize:
        x = x * 2


print(multiplyby2(), 's')

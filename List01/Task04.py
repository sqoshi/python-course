from Task02 import primes
from Task03 import removeDuplicates


def prime_factors(n):
    dividers = []
    while n != 1:
        for i in primes(n):
            if n % i == 0:
                n /= i
                dividers.append(i)
    dividers.sort()
    result = []
    for x in removeDuplicates(dividers):
        ctr = 0
        for y in dividers:
            if x == y:
                ctr += 1
        result.append((x, ctr))
    return result


print(prime_factors(123))

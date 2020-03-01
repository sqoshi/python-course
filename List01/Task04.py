from Task02 import primes
from Task03 import removeDuplicates


def prime_factors(n):
    dividers = []
    numbers = primes(n)
    while n != 1:
        for i in numbers:
            if n % i == 0:
                n /= i
                dividers.append(i)
    dividers.sort()
    withoutRep = removeDuplicates(dividers)
    result = []
    for x in withoutRep:
        ctr = 0
        for y in dividers:
            if x == y:
                ctr += 1
        result.append((x, ctr))
    return result


print(prime_factors(472))

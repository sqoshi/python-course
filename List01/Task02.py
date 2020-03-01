def primes(n):
    result = [i for i in range(2, n + 1)]
    for x in range(2, n + 1):
        for y in range(2, x):
            if x % y == 0:
                result.remove(x)
                break
    return result


print(primes(124))

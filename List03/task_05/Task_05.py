from itertools import combinations


def allSubsets(l):
    return sum(map(lambda r: list(combinations(l, r)), range(1, len(l) + 1)), [])


print(allSubsets([1, 2, 3, 4]))

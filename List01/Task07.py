from random import choice

from Task03 import removeDuplicates


def generateString(n):
    letters = ('a', 'b', 'c')
    return "".join(choice(letters) for i in range(n))


def generateList(n):
    return [generateString(n) for i in range(pow(3, n))]


def getDictionaryOfString(s):
    d = {}
    for i in range(len(s)):
        if s[i] != '*':
            d[i] = s[i]
    return d


def getSegments(l, p):
    d = getDictionaryOfString(p)
    segments = []
    print(d)
    for i in range(len(l)):
        S = getDictionaryOfString(l[i])
        if all(item in S.items() for item in d.items()):
            segments.append(l[i])
    return segments


def start(n):
    l = removeDuplicates(generateList(n))
    print(len(l), l)

    pattern = input()
    while len(pattern) != n:
        print('Pattern need to have ', n, ' symbols')
        pattern = input()
    seg = getSegments(l, pattern)
    print(seg)


start(8)

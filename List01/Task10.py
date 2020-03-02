from math import floor, pi, sin, cos, tan

from numpy.ma import arange


def print2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()


def getEmptyGraph(g, s):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] != '*':
                if j == s:
                    g[i][j] = '|'
                    if i == 0:
                        g[i][j] = '^'
                if i == floor(len(g) / 2):
                    g[i][j] = '-'
                    if j == floor(len(g[i]) - 1):
                        g[i][j] = '>'
                if i == floor(len(g) / 2) and j == s:
                    g[i][j] = '+'
    return g


def inRange(low, high, x):
    return low <= x <= high


def lin(x):
    return x


def draw(func, x1, x2):
    Dx = 80
    Dy = 24
    points = []
    nearZero = []
    yAxis = 0
    # znajdz punkty
    g = [[' ' for j in range(Dx)] for i in range(Dy)]
    for x in arange(x1, x2, ((abs(x1 - x2)) / Dx)):
        points.append(-floor(12 * func(x)) + int(len(g) / 2) - 1)
        if round(x) == 0:
            nearZero.append(abs(x))

    # USTAW OS
    if inRange(x1, x2, 0):
        m = min(nearZero)
        count = 0
        for x in arange(x1, x2, ((abs(x1 - x2)) / 80)):
            if abs(x) == m:
                yAxis = count
            count += 1

    # umiesc punkty
    for i in range(Dy):
        for j in range(Dx):
            if -abs(Dy) < points[j] < abs(Dy):
                g[points[j]][j] = '*'
            else:
                g[Dy - 1][j] = 'E'

    print2DArray(getEmptyGraph(g, yAxis))


draw(sin, -2 * pi, 1 * pi)

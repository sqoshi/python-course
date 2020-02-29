import scipy.special


def pascal_triangle(n):
    for x in range(n):
        print(2*(n - x + 1) * ' ', end='')
        for y in range(x + 1):
            print(int(scipy.special.binom(x, y)), ' ', end=' ')
        print()


pascal_triangle(6)

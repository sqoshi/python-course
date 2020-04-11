import math

funcs = []


def overload(func):
    funcs.append(func)

    def wrapper(*args, **kw):
        for x in funcs:
            try:
                res = x(*args, **kw)
            except TypeError as e:
                pass
        return res

    return wrapper


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2, 4)}")

print(f"norm(2,3,4) = {norm(2, 3, 4)}")

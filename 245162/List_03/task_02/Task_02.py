test = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]


def flatten(l):
    for x in l:
        if isinstance(x, list) \
                and not isinstance(x, (str, int, bytes)):
            for y in flatten(x):
                yield y
        else:
            yield x


#print(list(flatten(test)))

import random
from collections import deque

var = ["1",
       ["2", ["4", ["8", None, None], ["9", None, None]], ["5", None, None]],
       ["3", ["6", None, None], ["7", None, None]]]


def BFS(tree_):
    if tree_ is None:
        return
    que = deque([tree_])
    while que:
        t = que.pop()
        if t is None:
            continue
        yield t[0]
        que.append(t[1])
        que.append(t[2])


def DFS(tree_):
    if tree_ is None:
        return
    yield tree_[0]
    yield from DFS(tree_[1])
    yield from DFS(tree_[2])


def printTreeInOrder(tree):
    if tree[1] is not None:
        printTreeInOrder(tree[1])
    print(tree[0], end=", ")
    if tree[2] is not None:
        printTreeInOrder(tree[2])


def generateTree(h):
    if h == 0:
        return None
    val = random.randint(-(h ** 2), h ** 2)
    rh = generateTree(random.randint(0, h - 1))
    h = generateTree(h - 1)
    if random.choice([True, False]):
        return [val, rh, h]
    return [val, rh, h]


def main():
    ex = generateTree(5)
    printTreeInOrder(ex)
    print()
    print(list(BFS(ex)))
    print(list(DFS(ex)))
    print(ex)


main()

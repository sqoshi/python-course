import random
import collections


def rand_tree(h: int):
    if h == 0:
        return None
    elif h == 1:
        return Node(random.randint(-(h ** 2), h ** 2), [], 1)
    counter = random.randint(1, 2)
    sub_top_pos = random.randrange(0, counter)
    val = random.randint(-h ** 2, h ** 2)
    subs = []
    for i in range(counter):
        if i != sub_top_pos:
            _tree = rand_tree(random.randint(1, h - 1))
        else:
            _tree = rand_tree(h - 1)
        subs.append(_tree)

    return Node(val, subs, h)


class Node:
    def __init__(self, value, subs, h):
        self.value = value
        self.h = h
        self.subs = subs

    def __str__(self):
        return f'{self.value} h={self.h} [{", ".join(str(s) for s in self.subs)}]'

    def BFS(self):
        if self is None:
            return
        que = collections.deque([self])
        while que:
            tree = que.pop()
            yield tree.value
            que.extend(tree.subs)

    def DFS(self):
        if self is None:
            return
        yield self.value
        for tree in self.subs:
            yield from tree.DFS()


def main():
    example = rand_tree(4)
    print(example)
    print(list(example.BFS()))
    print(list(example.DFS()))


main()

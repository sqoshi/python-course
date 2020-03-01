def removeDuplicates(l):
    l = list(dict.fromkeys(l))
    return l


removeDuplicates([1, 1, 1, 2, 3, 3, 2, 2])

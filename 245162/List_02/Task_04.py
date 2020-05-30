#!/usr/bin/python

import sys
import hashlib
import os


def removeDuplicates(l):
    l = list(dict.fromkeys(l))
    return l


def t4(path):
    shpfiles = []
    tags = []
    sizes = []
    repsFiles = []

    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            shpfiles.append(os.path.join(dirpath, x))
            tags.append(hashlib.md5(x.encode()).hexdigest())
            sizes.append(os.path.getsize(os.path.join(dirpath, x)))
    print(shpfiles)
    for i in range(len(shpfiles)):
        for j in range(len(shpfiles)):
            if i != j and tags[i] == tags[j] and sizes[i] == sizes[j]:
                repsFiles.append(shpfiles[i])
    repsFiles = (removeDuplicates(repsFiles))
    print(repsFiles)


    # t4(sys.argv[1])


t4("/home/piotr/Documents/python-course/245162/List_02/tests/dir1")

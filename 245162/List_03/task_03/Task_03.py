from task_02.Task_02 import flatten


def summer(filename):
    f = open(filename, "r")
    result = []
    content = f.readlines()
    for line in content:
        temp = line.split()
        res = list(flatten(temp))
        result.append(res[len(res) - 1])
    print('Całkowita liczba bajtów:', sum(list(map(int, result))))


summer("test")

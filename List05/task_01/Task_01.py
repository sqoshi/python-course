import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def my_round(flo):
    i = int(flo)
    rest = abs(flo - i)
    if rest <= 25:
        addition = 0
    elif 0.75 > rest > 0.25:
        addition = 0.5
    else:
        addition = 1.0
    return i + addition


def get_y():
    y = np.array([])
    with open("../data/ml-latest-small/ratings.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        counter = 0
        for row in reader:
            if row[1] == "1":
                y = np.append(y, float(row[2]))
                counter += 1
    return y  # .reshape(-1, 1)


def get_ids(m):
    people_ids = []
    movie_ids = []
    with open("../data/ml-latest-small/movies.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader):
            if m >= i:
                if i > 1:
                    movie_ids.append(row[0])
            else:
                break

    with open("../data/ml-latest-small/ratings.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[1] == "1":
                people_ids.append(row[0])

    return people_ids, movie_ids


def get_x(p, m):
    x = [[0 for _ in range(len(m))] for _ in range(len(p))]
    with open("../data/ml-latest-small/ratings.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] in p and row[1] in m:
                x[p.index(row[0])][m.index(row[1])] = float(row[2])
    x = np.array(x)
    return x


def main():
    y = get_y()
    people_ids, movies_ids = get_ids(100)
    x = get_x(people_ids, movies_ids)
    z = [i for i in range(len(people_ids))]
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
    # for i in range(len(y_pred)):
    #   y_pred[i] = my_round(y_pred[i])
    print('predicted response:', y_pred, sep='\n')
    print('Real response:', y, sep='\n')
    plt.scatter(z, y, color="red")
    plt.plot(z, y_pred, color="green")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


main()

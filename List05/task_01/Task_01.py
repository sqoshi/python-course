import csv
import sys

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def my_round_all(y_pred):
    """Rounding all grades as secyfied in my_round"""
    for i in range(len(y_pred)):
        y_pred[i] = my_round(y_pred[i])


def my_round(flo):
    """Rounds marks to halves (0.5)."""
    if flo >= 5:
        return 5
    if flo <= 1:
        return 1
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
    """Founds array 1xn( In this case n=215).
    It is a grades group of movie with movieId == 1 (Toy Story).
     Information that we can get from rating.csv"""
    y = np.array([])
    people_ids = []
    with open("../data/ml-latest-small/ratings.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        counter = 0
        for row in reader:
            if row[1] == "1":
                y = np.append(y, float(row[2]))
                people_ids.append(row[0])
                counter += 1

    return people_ids, y  # .reshape(-1, 1)


def get_movie_ids(m):
    """Gets first m movie ids from movies.csv."""
    movie_ids = []
    with open("../data/ml-latest-small/movies.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader):
            if m >= i:
                if i > 1:
                    movie_ids.append(row[0])
            else:
                break
    return movie_ids


def get_x(people_ids, movie_ids):
    """Gets x which is a matrix that contains ratings of movies that ids were given
    for people whose ids were also given. """
    x = [[0 for _ in range(len(movie_ids))] for _ in range(len(people_ids))]
    with open("../data/ml-latest-small/ratings.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] in people_ids and row[1] in movie_ids:
                x[people_ids.index(row[0])][movie_ids.index(row[1])] = float(row[2])
    x = np.array(x)
    return x


def a(round, graphs):
    name = 'a'
    graphs_data = []
    samples = [10, 100, 1000]
    for m in samples:
        people_ids, y = get_y()
        size = (len(people_ids))
        movies_ids = get_movie_ids(m)
        x = get_x(people_ids, movies_ids)
        model = LinearRegression().fit(x, y)
        r_sq = model.score(x, y)
        print('##########################################################################################')
        print('###################################### m =', m, '############################################')
        print('##########################################################################################')
        print('coefficient of determination:', r_sq)
        print('intercept:', model.intercept_)
        print('slope:', model.coef_)
        y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
        # I am not really sure if i should round my results or not.
        graphs_data.append((y, y_pred))
        if round:
            name = "a_rounded"
            my_round_all(y_pred)
        print('Predicted response:', y_pred, sep='\n')
        print('Real response:', y, sep='\n')
    if graphs:
        i = 0
        fig, l = plt.subplots(len(graphs_data))

        for real, pred in graphs_data:
            z = [i for i in range(size)]
            l[i].scatter(z, real, color="red", s=3)
            # as line just for better visualisation i know there is no user 215,5 just R.
            l[i].plot(z, pred, color="green")
            i += 1
        fig.savefig('plots/' + name)
        plt.show()


def b(round, graphs):
    name = 'b'
    graphs_data = []
    for m in [10, 100, 500, 1000, 10000]:
        people_ids, y = get_y()
        movies_ids = get_movie_ids(m)
        x = get_x(people_ids, movies_ids)
        x_train, x_test, y_train, y_test = x[:200], x[200:], y[:200], y[200:]
        model = LinearRegression().fit(x_train, y_train)
        y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
        # I am not really sure if i should round my results or not.
        if round:
            my_round_all(y_pred)
            name = 'b_rounded'
        graphs_data.append((y_test, y_pred[200:]))
        print('======== Real | Predicted =======')
        for i in range(len(y_test)):
            print(y_test[i], " | ", y_pred[200 + i])
        print('=================================')

    if graphs:
        i = 0
        fig, l = plt.subplots(len(graphs_data))
        for real, pred in graphs_data:
            z = [i for i in range(15)]
            l[i].plot(z, real, color="red", )
            l[i].plot(z, pred, color="green")
            i += 1
        fig.savefig('plots/' + name)
        plt.show()


def main(options):
    if "a" in options:
        f = a
    elif "b" in options:
        f = b
    else:
        raise ValueError('You need to pass arguments. For example a --graphs --round')

    if "--graphs" in options and "--round" in options:
        f(True, True)
    elif "--graphs" in options and "--round" not in options:
        f(False, True)
    elif "--round" in options and "--graphs" in options:
        f(True, False)
    else:
        f(False, False)


main(sys.argv[1:])

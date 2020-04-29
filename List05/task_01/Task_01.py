import csv
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def my_round_all(y_pred):
    # rounding i am  not really sure if i should do it.
    for i in range(len(y_pred)):
        y_pred[i] = my_round(y_pred[i])


def my_round(flo):
    """Rounds marks to halves (0.5)."""
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


def a():
    for m in [10, 100, 100]:
        people_ids, y = get_y()
        movies_ids = get_movie_ids(m)
        x = get_x(people_ids, movies_ids)
        # just for graph?
        z = [i for i in range(len(people_ids))]
        model = LinearRegression().fit(x, y)
        r_sq = model.score(x, y)
        print('##########################################################################################')
        print('###################################### m =', m, '############################################')
        print('##########################################################################################')
        print('coefficient of determination:', r_sq)
        print('intercept:', model.intercept_)
        print('slope:', model.coef_)
        y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)

        print('Predicted response:', y_pred, sep='\n')
        print('Real response:', y, sep='\n')
        plt.scatter(z, y, color="red")
        plt.plot(z, y_pred, color="green")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()


def b():
    for m in [10, 100, 500, 100, 1000, 10000]:
        people_ids, y = get_y()
        movies_ids = get_movie_ids(m)
        x = get_x(people_ids, movies_ids)
        x_train, x_test, y_train, y_test = x[:200], x[200:], y[:200], y[200:]
        model = LinearRegression().fit(x_train, y_train)
        y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
        my_round_all(y_pred)
        print('Predicted response:', y_pred[200:], sep='\n')
        print('Real response:', y_test, sep='\n')


def main():
    b()


main()

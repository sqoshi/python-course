from scipy.sparse import csr_matrix
import numpy as np
import csv
import pandas as pd

np.seterr(divide='ignore', invalid='ignore')


def read_movie_all():
    df = pd.read_csv('../data/ml-latest-small/movies.csv')
    movies = df.movieId
    return list(movies)


def read_user_all():
    df = pd.read_csv('../data/ml-latest-small/ratings.csv')
    users = df.userId
    users = list(dict.fromkeys(users))
    return list(dict.fromkeys(users))


def get_x(users, movie_ids):
    x = [[0 for _ in range(len(movie_ids))] for _ in range(len(users))]
    with open("../data/ml-latest-small/ratings.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] in users and row[1] in movie_ids:
                x[users.index(row[0])][movie_ids.index(row[1])] = float(row[2])
    x = csr_matrix(x)
    return x


def main():
    movie_ids = read_movie_all()
    user_ids = read_user_all()
    x = (get_x(user_ids, movie_ids))
    for el in x:
        print(el)


main()

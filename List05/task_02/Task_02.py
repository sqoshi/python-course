import csv
import tkinter as tk
import numpy as np
import tkinter.font

np.seterr(divide='ignore', invalid='ignore')


def read_movie_all():
    movies = []
    with open('../data/ml-latest-small/movies.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if int(row[0]) >= 10000:
                break
            movies.append((row[0], row[1]))
    return movies


def read_user_all():
    users = []
    with open('../data/ml-latest-small/ratings.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if row[0] not in users:
                users.append(row[0])
    return users


def get_x(users, movie_ids):
    x = [[0 for _ in range(len(movie_ids))] for _ in range(len(users))]
    with open("../data/ml-latest-small/ratings.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] in users and row[1] in movie_ids:
                x[users.index(row[0])][movie_ids.index(row[1])] = float(row[2])
    x = np.array(x)
    return x


def gui(movies_titles, movies_ids):
    rated = []
    global y
    y = [[0] for _ in range(len(movies_titles))]

    def dbclick(event):
        global movie_title
        item = listbox.get('active')
        movie_title = item
        decline_cmdr[item]()

    def reset():
        global y
        y = [[0] for _ in range(len(movies_titles))]

    def clicked():
        val = int(rate_grade.get())
        position = movies_titles.index(movie_title)
        rated.append(movie_title)
        y[position][0] = val
        print('You rated', movie_title, '!', val)

    def recommend():
        q = 10
        fontStyle = tk.font.Font(family="Lucida Grande", size=8)
        if len(rated) > 0:
            users = read_user_all()
            x = get_x(users, movies_ids)
            z = np.nan_to_num(np.dot(np.nan_to_num(np.nan_to_num(x) / np.nan_to_num(np.linalg.norm(x, axis=0))),
                                     np.nan_to_num(np.nan_to_num(np.array(y)) / np.nan_to_num(np.linalg.norm(y)))))
            X = np.nan_to_num(np.nan_to_num(x) / np.nan_to_num(np.linalg.norm(x, axis=0)))
            Z = z / np.linalg.norm(z)
            cos = np.dot(X.T, Z)
            result = []
            for i in range(len(cos)):
                result.append((cos[i][0], movies_ids[i], movies_titles[i]))
            sorted_result = sorted(result, key=lambda p: p[0])
            h = 100
            for j in range(len(sorted_result) - 1, len(sorted_result) - q, -1):
                tk.Label(master,
                         text=sorted_result[j][2], fg="orange", bg="black", font=fontStyle, width=32). \
                    place(x=10, y=h)
                h += 30

        else:
            print('You did not rated any movie.')

    master = tk.Tk()
    master.geometry("500x500")
    master.resizable(0, 0)  #
    scrollbar = tk.Scrollbar(master)
    scrollbar.pack(side='right', fill='y')

    menubar = tk.Menu(master)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Reset", command=reset)
    filemenu.add_command(label="Exit", command=master.quit)
    menubar.add_cascade(label="Menu", menu=filemenu)
    master.config(menu=menubar)

    tk.Button(master, text="Get Recommendation", command=recommend).place(x=40, y=30)
    tk.Button(master, text="Rate", command=clicked).place(x=90, y=430)

    rate_grade = tk.Scale(master, from_=0.0, to=5.0, orient=tk.HORIZONTAL, length=200, digits=2)
    rate_grade.place(x=20, y=380)

    listbox = tk.Listbox(master, yscrollcommand=scrollbar.set, width=30)
    decline_cmdr = {}

    for item in movies_titles:
        listbox.insert('end', item)
        decline_cmdr[item] = lambda i=item: print()

    listbox.pack(side='right', fill='both')
    scrollbar.config(command=listbox.yview)
    listbox.bind('<Double-1>', dbclick)

    master.mainloop()


def main():
    movies_ids, movies_titles = zip(*read_movie_all())
    gui(movies_titles, movies_ids)


main()

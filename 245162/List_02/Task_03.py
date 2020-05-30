import os


# ls -p | grep -v / | rename 'y/A-Z/a-z/'
def change(path):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.'):
                os.replace(entry.name, entry.name.lower())  # upper


change("/home/piotr/Documents/python-course/List02/task_03")

import os

# ls -p | grep -v / | rename 'y/A-Z/a-z/'

path = "/home/piotr/Documents/python-course/List02/task_03"
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.'):
            os.replace(entry.name, entry.name.lower())#upper 

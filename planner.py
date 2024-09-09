import csv

def read_tasks(filename):
    tasks = {}
    for row in csv.reader(open(filename)):
        number = int(row[0])
        title = row[1]
        duration = float(row[2])
        prerequisites = row[3]
        tasks[number] = (title, duration, \
                        prerequisites)
    return tasks

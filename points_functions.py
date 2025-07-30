def points(database, id, win=False):
    streak = int(database[id][2])
    points = int(database[id][4])
    if win:
        points += streak+8
        database[id][2] = streak+1
    else:
        points -= 5
        database[id][2] = 0
    database[id][4] = points
    
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
    

def points_especial(database, id, type):
    points = int(database[id][4])
    if type == 0:
        points += 2
    elif type == 1:
        points += 3
    elif type == 2:
        points += 5
    if type == 3:
        points += 5
    elif type == 4:
        points += 3
    elif type == 5:
        points += 5
    elif type == 6:
        major = int(database[id][5])+1
        points += 8
        database[id][5] = major
    database[id][4] = points
    
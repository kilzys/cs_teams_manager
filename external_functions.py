import pandas as pd
import openpyxl

def criarExcel(database):
    index = []
    names = []
    wins = []
    streak = []
    loses = []
    points = []
    majors = []
    for item in database:
        index.append(item)
        names.append(database[item][0])
        wins.append(database[item][1])
        streak.append(database[item][2])
        loses.append(database[item][3])
        points.append(database[item][4])
        majors.append(database[item][5])
    print(index,names,wins,streak,loses,points,majors)
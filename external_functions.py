import pandas as pd
import openpyxl

def criarExcel(database):
    values = separar_planilha(database)
    ranking = []
    for items in values[0]:
        ranking.append(items+1)
    file = pd.DataFrame({'Ranking': ranking,
                        'Team': values[1],
                         'Wins': values[2],
                         'Streak': values[3],
                         'Loses': values[4],
                         'Points': values[5],
                         'Majors': values[6]})
    file.to_excel('hltv.xlsx', 'teams_database')


def exibir_teams(database):
    values = separar_planilha(database)
    file = pd.DataFrame({'Team': values[1],
                         'Wins': values[2],
                         'Streak': values[3],
                         'Loses': values[4],
                         'Points': values[5],
                         'Majors': values[6]})
    print(file)


def separar_planilha(database):
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
    return index,names,wins,streak,loses,points,majors
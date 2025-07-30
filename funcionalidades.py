from db_manipulation import atualizar_banco
from files_functions import write

def interface(database):
    while True:
        print('\033[32m[0] - Visualizar Times\033[m')
        print('\033[32m[1] - Registrar Novo Time\033[m')
        print('\033[31m[2] - Atualizar Time\033[m')
        print('\033[31m[3] - Excluir Time\033[m')
        print('\033[32m[4] - Sair\033[m')
        option = input(': ')
        if option == '0':
            visualizar(database)
        elif option == '1':
            registrar(database)
            dados_brutos = atualizar_banco(database)
            write('database.txt', dados_brutos)
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            break
        else:
            print('\033[31mOpção indisponível\033[m')


def visualizar(database):
    index = 0
    for team in database:
        if index == 0 or index%2 == 0:
            print(f'\033[47m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        else:
            print(f'\033[1;30m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        index+=1


def registrar(database):
    while True:
        temp = []
        index = len(database)
        team = input('Team: ')
        team_w = input('Wins: ')
        team_s = input('Streak: ')
        team_l = input('Loses: ')
        team_p = input('Points: ')
        team_m = input('Majors: ')
        confirm = input('\033[31mConfirmar novo time? [s/n] \033[m')
        if confirm in 'Ss':
            temp = [team, team_w, team_s, team_l, team_p, team_m]
            database[index] = temp.copy()
            return
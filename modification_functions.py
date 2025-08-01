from points_functions import *
from files_functions import write
from db_manipulation import atualizar_banco
from external_functions import exibir_teams

def menu_modf(database):
    while True:
        exibir_teams(database)
        print('\033[35m[0] - Dev Modifications\033[m')
        print('\033[33m[1] - Atualizar Time\033[m')
        print('\033[32m[2+] - Cancelar/Finalizar\033[m')
        option = int(input(': '))
        if option == 0:
            dev_function(database)
            sincronizar(database)
        elif option == 1:
            update_time(database)
            sincronizar(database)
        elif option == 9991:
            zerar_banco(database)
            sincronizar(database)
        else:
            return


def update_time(database):
        team = selecionar_time()
        if team != 999:
            menu_sincronizar(team, database)
        else:
             return


def selecionar_time():
        print('Digite o ID do time: [999 para cancelar] ')
        id_team = int(input(': '))
        return id_team


def menu_sincronizar(id, database):
    while True:
        print(f'\033[34m  {database[id][0]}  \033[m')
        print(f'\033[34m  Wins: {database[id][1]}  \033[m')
        print(f'\033[34m  Streak: {database[id][2]}  \033[m')
        print(f'\033[34m  Loses: {database[id][3]}  \033[m')
        print(f'\033[34m  Points: {database[id][4]}  \033[m')
        print(f'\033[34m  Majors: {database[id][5]}  \033[m')
        print('[0] +1 Win')
        print('[1] +1 Lose')
        print('[2] Special Event')
        print('\033[31m[3+] to cancel/confirm\033[m')
        option = int(input(': '))
        if option == 0:
            database[id][1] = int(database[id][1])+1
            points(database, id, True)
        elif option == 1:
            database[id][3] = int(database[id][3])+1
            points(database, id)
        elif option == 2:
            valor = special_interface()
            if valor != 'null':
                points_especial(database, id, valor)
        else:
            return


def visualizar(database):
    index = 0
    for team in database:
        if index == 0 or index%2 == 0:
            print(f'\033[47m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        else:
            print(f'\033[1;30m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        index+=1


def dev_function(database):
    exibir_teams(database)
    id = int(input('Team ID: '))
    while True:
        print(f'\033[34m[0] - {database[id][0]}  \033[m')
        print(f'\033[34m[1] - Wins: {database[id][1]}  \033[m')
        print(f'\033[34m[2] - Streak: {database[id][2]}  \033[m')
        print(f'\033[34m[3] - Loses: {database[id][3]}  \033[m')
        print(f'\033[34m[4] - Points: {database[id][4]}  \033[m')
        print(f'\033[34m[5] - Majors: {database[id][5]}  \033[m')
        print('\033[31m[6+] - FINALIZAR\033[m')
        option = int(input(': '))
        if option >= 6:
            return
        elif option == 0:
            new_info = input(f'Team Name: ')
        elif option == 1:
            new_info = input(f'Wins: ')
        elif option == 2:
            new_info = input(f'Streak: ')
        elif option == 3:
            new_info = input(f'Loses: ')
        elif option == 4:
            new_info = input(f'Points: ')
        elif option == 5:
            new_info = input(f'Majors: ')
        confirm = input('\033[31mConfirmar a mudaçna dos dados? [s/n]\033[m ')
        if confirm in 'Ss':
            database[id][option] = new_info
        else:
            print('\033[31mCancelando a mudança...\033[m')


def zerar_banco(database):
    for time in database:
        team_name = database[time][0]
        database[time] = [team_name,0,0,0,0,0]
    print('\033[41mFunção de admin utilizada, banco de dados zerado para todos os times existente.\033[m')


def special_interface():
    print('\033[32m[0] - Vitória nas Quartas')
    print('[1] - Vitória nas SemiFinais')
    print('[2] - Ganhou um Torneio')
    print('\033[35m[3] - Chegou nas Playoffs de Major')
    print('[4] - Vitória nas Quartas de Major')
    print('[5] - Vitória nas Semifinais de Major')
    print('[6] - Venceu o Major')
    print('\033[m[999] - Cancelar')
    option = int(input(': '))
    if option != 999:
        return option
    else:
        return 'null'
    

def sincronizar(database):
    dados_brutos = atualizar_banco(database)
    write('database.txt', dados_brutos)
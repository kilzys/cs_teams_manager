from db_manipulation import atualizar_banco
from files_functions import write
from modification_functions import *

def interface(database):
    while True:
        print('\033[32m[0] - Visualizar Times\033[m')
        print('\033[32m[1] - Registrar Novo Time\033[m')
        print('\033[33m[2] - Atualizar Time\033[m')
        print('\033[32m[3] - Excluir Time\033[m')
        print('\033[32m[4] - Sair\033[m')
        option = input(': ')
        if option == '0':
            visualizar(database)
        elif option == '1':
            registrar(database)
            sincronizar_database(database)
        elif option == '2':
            visualizar(database)
            menu_modf(database)
        elif option == '3':
            visualizar(database)
            excluir(database)
            sincronizar_database(database)
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
        print('\033[31mSe desejar cancelar, digite "999" no nome do time\033[m')
        team = input('Team: ')
        if team == '999':
            return
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


def excluir(database):
    print('\033[31mDigite 9999 para cancelar\033[m')
    id = int(input('Digite o ID do time que deseja excluir: '))
    if id == 999:
        return
    for item in range(len(database)):
        if item >= id:
            if item == len(database)-1:
                del database[item]
            else:
                database[item] = database[item+1]


def sincronizar_database(database):
    dados_brutos = atualizar_banco(database)
    write('database.txt', dados_brutos)
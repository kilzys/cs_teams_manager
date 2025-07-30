def menu_modf(database):
    while True:
        visualizar(database)
        print('\033[35m[0] - Dev Modifications\033[m')
        print('\033[33m[1] - Atualizar Time\033[m')
        print('\033[32m[2+] - Cancelar\033[m')
        option = int(input(': '))
        if option > 1:
            return
        elif option == 0:
            dev_function(database)
        elif option == 1:
            update_time(database)


def update_time(database):
        team = selecionar_time()
        if team != 000:
            menu_sincronizar(team, database)
        else:
             return


def selecionar_time():
        print('Digite o ID do time: [000 para cancelar] ')
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
        elif option == 1:
            database[id][3] = int(database[id][3])+1
        elif option == 2:
            pass
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
    visualizar(database)
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
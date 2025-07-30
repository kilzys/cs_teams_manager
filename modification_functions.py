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
            pass
        elif option == 1:
            update_time(database)


def update_time(database):
        team = selecionar_time()
        if team != 000:
            menu_sincronizar(team, database)
        else:
             return


def selecionar_time():
        print('Digite o ID do time: [000 para cancelar]')
        id_team = int(input(': '))
        return id_team


def menu_sincronizar(id, database):
    while True:
        print(f'\033[43m  {database[id][0]}  \033[m')
        print('[0] +1 Win')
        print('[1] +1 Lose')
        print('[2] Special Event')
        print('\033[31m[3+] to cancel\033[m')
        option = int(input(': '))
        if option == 0:
            database[id][1] = int(database[id][1])+1
        elif option == 1:
            pass
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
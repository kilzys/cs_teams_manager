def interface(database):
    while True:
        print('\033[32m[0] - Visualizar Times\033[m')
        print('\033[31m[1] - Registrar Novo Time\033[m')
        print('\033[31m[2] - Atualizar Time\033[m')
        print('\033[31m[3] - Excluir Time\033[m')
        print('\033[32m[4] - Sair\033[m')
        option = input(': ')
        if option == '0':
            visualizar(database)
        elif option == '1':
            pass
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
            print(f'\033[47mID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]}\033[m')
        else:
            print(f'\033[1;30mID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]}\033[m')
        index+=1
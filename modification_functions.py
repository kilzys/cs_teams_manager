def menu_modf(database):
    while True:
        print('[999] - Cancelar')
        print('[0] - Modificar informação do time')
        print('[1] - Sincronizar Time')
        option = int(input(': '))
        if option == 999:
            return
        elif option == 0:
            pass
        elif option == 1:
            update_time(database)


def update_time(database):
    while True:
        break


def selecionar_time(database):
    while True:
        print('Digite o ID do time: [999 para cancelar]')
        break
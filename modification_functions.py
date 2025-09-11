from points_functions import *
from files_functions import write
from db_manipulation import atualizar_banco
from external_functions import exibir_teams

# Segunda interface, voltada para funções e macanismos de atualização dos arquivos já existentes

# Observação -> É importante notar que, a cada iteração com o sistema, a única parte em que os dados são de fato salvos, é após a execução das funções "principais". Isso fica claro quando, após cada interface (uma após a outra), vemos a falta da função "sincronizar". Isso não foi um problema até o momento para ser honesto, até porque, para você sair do programa, é necessário voltar. E, ocasionalmente, você voltará para a parte "principal", onde temos a primeira interface.


def menu_modf(database):
    while True:
        # Exibição padrão, com cada opção garantindo a execução de uma função "sincronizar", como na interface anterior. Isso para evitar erros de sincronismo entre as execuções das diversas funções do programa, seja qual for a ordem de utilização.
        exibir_teams(database)
        print('\033[35m[0] - Dev Modifications\033[m')
        print('\033[33m[1] - Atualizar Time\033[m')
        print('\033[32m[2+] - Cancelar/Finalizar\033[m')
        option = int(input(': '))
        match option:
            case 0:
                dev_function(database)
                sincronizar(database)
            case 1:
                update_time(database)
                sincronizar(database)
            case 9991:
                zerar_banco(database)
                sincronizar(database)
            case _:
                return


# Função simples, que chama uma outra
def update_time(database):
        # Cria uma variável e guarda o resultado do return dela. Essa variável chamada é bem simples, e de fato não possui nada demais, nem motivo para separação dessa aqui. Porém, foi escolhido assim por motivos de legibilidade.
        team = selecionar_time()
        # Se o time for diferente de 999, ele irá chamar uma outra função, de outra interface, dessa vez direcionada as oções de modificação.
        if team != 999:
            menu_sincronizar(team, database)
        else:
             return

# Função selecionada após a "update_time". A única funcionalidade dela aqui é, única e exclusivamente, deixar a função anterior com legibilidade alta.
def selecionar_time():
        print('Digite o ID do time: [999 para cancelar] ')
        id_team = int(input(': '))
        return id_team


# Função chamada para mostrar uma nova interface destinada à modificação do time selecionado
def menu_sincronizar(id, database):
    while True:
        # Mostra as informações atual do time selecionado, além de opções sobre modificações a nível de usuário
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
        match option:
            case 0:
                # Envia para a função points o id do time selecionado, com o parâmetro "True" ativada, significando que é de fato uma vitória e não uma derrota. Além disso, aqui mesmo já é puxado as vitórias e somado +1 para ela.
                database[id][1] = int(database[id][1])+1
                points(database, id, True)
            case 1:
                # Mesmo procedimento realizado acima. A única diferença é que aqui a derrota que é puxada e aumentada em 1, juntamente do parâmetro "false" or "null".
                database[id][3] = int(database[id][3])+1
                points(database, id)
            case 2:
                # Aqui uma nova função é chamada, responsável pela interface dos pontos especiais. Ele pega o retorno da opção selecionada e chama outra função, que irá atualizar os pontos com base nos parâmetros passados. Valor é o tipo de evento que deve ocorrer. Id é o id do time, e o database é o nome do arquivo
                valor = special_interface()
                if valor != 'null':
                    points_especial(database, id, valor)
            case _:
                return


# FUNÇÃO AGORA OBSOLETA
'''def visualizar(database):
    index = 0
    for team in database:
        if index == 0 or index%2 == 0:
            print(f'\033[47m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        else:
            print(f'\033[1;30m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        index+=1'''


# Aqui temos uma nova interface, essa é a da parte de devs. Mostramos na tela os times já registrado e suas informações. Como é uma função de admin/dev, temos uma interface mais "pobre". O interessante aqui é que podemos simplesmente modificar qualquer informação do time selecionado, basta passar a opção que você selecionou.
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
        # Não foi atualizado para a formatação *match*, pois possui o *>=*
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
            # Apenas uma forma de garantir que a mudança será feita de forma segura, e após a confirmação da mudança
            database[id][option] = new_info
        else:
            print('\033[31mCancelando a mudança...\033[m')


# Quando chamada, ela simplesmente zero todos os dados de todos os times. Nenhum time fica de fora, todos tem seus dados voltados para 0. Nenhum time, porém, é excluído.
def zerar_banco(database):
    for time in database:
        team_name = database[time][0]
        database[time] = [team_name,0,0,0,0,0]
    print('\033[41mFunção de admin utilizada, banco de dados zerado para todos os times existente.\033[m')


# Interface especial, chamada após uma interface anterior. Essa interface aqui tem somente uma função, mostrar na tela a opção em número, e o que aquele número fará. O resultado irá retornar qual o evento que o usuário deseja ativar.
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
    
# Função extremamente importante para manter os dados após cada utilização de função
def sincronizar(database):
    dados_brutos = atualizar_banco(database)
    write('database.txt', dados_brutos)
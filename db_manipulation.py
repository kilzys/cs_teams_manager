from files_functions import *

def obter_banco(database_name):
    # Criação das variáveis banco e index
    database = {}
    index = 0

    # Pegando os dados brutos e fazendo a primeira formatação, tornando todos que possuem '\n' em uma lista
    dados_brutos = read(database_name)
    split_dados = dados_brutos.split('\n')

    # Para cada item na lista split_dados, será tirado as ',' tornando cada item de fato um valor, em vez de uma string própria. Também adiciona a nova lista na database
    for team in split_dados:
        temp = team.split(',')
        database[index] = temp.copy()
        index+=1
        temp.clear()

    # Retorno da database formatada
    return database


def atualizar_banco(database):
    dadosbrutos = ''
    for item in database:
        if item == 0:
            dadosbrutos = f'{database[0][0]},{database[0][1]},{database[0][2]},{database[0][3]},{database[0][4]},{database[0][5]}'
        else:
            dadosbrutos = f'{dadosbrutos}\n{database[item][0]},{database[item][1]},{database[item][2]},{database[item][3]},{database[item][4]},{database[item][5]}'
    return dadosbrutos
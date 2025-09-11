from files_functions import *

# Função com o objetivo de manipulação dos dados para poder trabalhar no programa. Uma delas pega os dados brutos e os transformar em um dicionário para ser utilizado, enquanto o outro pega o dicionário e o transforma em dados brutos para ser salvo.


# Pega os dados brutos e os transforma.
def obter_banco(database_name):
    # Criação das variáveis banco e index.
    database = {}
    index = 0

    # Pegando os dados brutos e fazendo a primeira formatação, tornando todos que possuem '\n' em uma lista.
    dados_brutos = read(database_name)
    split_dados = dados_brutos.split('\n')

    # Para cada item na lista split_dados (já contendo os times separados), será tirado as ',' separando os diversos dados de cada time para poder ser tratado. Também adiciona a nova lista na database. (Exemplo: split_dados = [['team1,2,3,4,5']['team2,4,3,2']] -> [['team',2,3,4,5]['team2',2,4,3,2]]).
    for team in split_dados:
        # Exemplo -> ['team,2,3,4'] -> ['team',2,3,4].
        temp = team.split(',')
        # Salva nova lista na database criada anteriormente.
        database[index] = temp.copy()
        # Passa para o próximo index para continuar até o último time.
        index+=1
        # Limpa a variável temporária para evitar duplicações.
        temp.clear()

    # Retorno da database formatada.
    return database


# Aqui é feito o processo reverso, onde pegaresmos os dados completos e iremos transformar em dados brutos.
def atualizar_banco(database):
    # Variável em forma de "string", responsável por salvar os dados brutos.
    dadosbrutos = ''
    # Pegando cada time registrado na database.
    for item in database:
        # Verificando se é o primeiro time a ser registrado.
        if item == 0:
            # Sendo o primeiro, somente iremos salvar os dados em forma de "string". A questão é, precisamos manter a "," entre cada dado do time, para futura transformação desses dados brutos de volta em forma de dicionário. Aqui nós pegamos o [0][dados] pois é o primeiro item da dabatase, seguido de cada dado daquele time em seguida -> [0[1][2][3][4][5].
            dadosbrutos = f'{database[0][0]},{database[0][1]},{database[0][2]},{database[0][3]},{database[0][4]},{database[0][5]}'
        # Faz a mesma coisa que o comando acima, a única diferença aqui é quanto ao time passado, que não será mais [0][dados], mas sim [item][dados], seguindo a mesma sequencia acima. Importante relembrar, como não é mais o primeiro time, precisamos salvar esses novos dados juntamente dos salvos anteriormente, sendo necessário o {dadosbrutos} juntamente do '\n' para garantir que os dados anteriores serão salvos. O '\n' será utilizado para separar um time do outro, logo, é de suma importância mantê-lo.
        else:
            dadosbrutos = f'{dadosbrutos}\n{database[item][0]},{database[item][1]},{database[item][2]},{database[item][3]},{database[item][4]},{database[item][5]}'
    # Retorna esse banco de dados tratados.
    return dadosbrutos
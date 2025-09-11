from db_manipulation import atualizar_banco
from files_functions import write
from modification_functions import *
from external_functions import exibir_teams

# Função responsável pela interface principal do programa.

# Observação: É importante já deixar notificado aqui que o parâmetro utilizado por 90% das funções como cancelamento/retorno é justamente o número 999. Caso o arquivo/banco de dados ultrapasse ou, idealmente, se aproxime disso, será necessária a troca de todos esses valores para algo como '9999', ou até mais se o foco é evitar mudanças, ao mesmo tempo que o arquivo abriga milhares de valores.


def interface(database):
    while True:
        # Mostra as opções disponíveis
        # Podemos perceber que todas as opções, com exceção da '0' e da '4', chamam uma outra função, além da exclusiva, a função "sincronizar".   
        print('\033[32m[0] - Visualizar Times\033[m')
        print('\033[32m[1] - Registrar Novo Time\033[m')
        print('\033[33m[2] - Atualizar Time\033[m')
        print('\033[32m[3] - Excluir Time\033[m')
        print('\033[32m[4] - Sair\033[m')
        option = input(': ')
        match option:
            case '0':
                exibir_teams(database)
            case '1':
                registrar(database)
                sincronizar_database(database)
            case '2':
                # Chama uma outra parte de interface, já voltada exclusivamente para alterações de times, tanto como dev quanto como usuário
                menu_modf(database)
                sincronizar_database(database)
            case '3':
                # Primeiro ele exibe os times, para selecionar qual será excluído
                exibir_teams(database)
                excluir(database)
                sincronizar_database(database)
            case '4':
                break
            case _:
                # Em caso de outra opção selecionada
                print('\033[31mOpção indisponível\033[m')


# Antiga função de visualizar os times disponíveis/registrados no arquivo/sistema; porém, após a última atualização, uma nova funcionalidade de exibição foi criada, uma bem mais intuitiva e clara, rapidamente tomando o lugar dessa antiga função, agora obsoleta. Ela está aqui para possível aprimoração futura, visto que ela possui uma funcionalidade interessante que a nova não tem, a possiblidade de cores de fundo diversas a cada linha, colaborando para a visualização de diversos dados.
"""def visualizar(database):
    index = 0
    for team in database:
        if index == 0 or index%2 == 0:
            print(f'\033[47m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        else:
            print(f'\033[1;30m ID: {team} | Team: {database[team][0]}| Wins: {database[team][1]} | Streak: {database[team][2]} | Loses: {database[team][3]} | Points: {database[team][4]} | Majors: {database[team][5]} \033[m')
        index+=1
"""


# Registra novos times no arquivo
def registrar(database):
    while True:
        # Cria uma lista
        temp = []
        # Pega o tamanho total do arquivo
        index = len(database)
        print('\033[31mSe desejar cancelar, digite "000" no nome do time\033[m')
        team = input('Team: \033[34m')
        # Se for '000', ele cancela na hora, e retorna nulo
        if team == '000':
            return
        # Se passar pela primeira etapa, é chamado uma função de verificar duplicidade, que irá retornar o nome após a verificação (seja ele o mesmo, um outro, ou 000 em caso de cancelamento)
        team = verificar_duplicidade(database, team)
        # Verifica se o nome do time é '000' (lembrando que tudo aqui está sendo tratado como string, por isso não ocorre erro do '000' ser confundido por '0'). Se for, ele retorna vazio, senão, ele mantém a execução. Como a atribuição do novo time é feito dentro dessa mesma função, o retorno nulo não mudará nada, apenas quebrará o looping
        if team == '000':
            return
        # Função de confirmação
        confirm = input('\033[31mConfirmar novo time? [s/n] \033[m')
        if confirm in 'Ss':
            # Atribui o novo time com dados zerados
            temp = [team,0,0,0,0,0]
            # Insere esse novo time com os novos dados no final do dicionário passado. E aqui, o fato do len(arquivo) sempre retornar um valor mais alto (+1), não precisamos fazer nenhum cálculo ou lógica adicional, apenas utilizar esse index como último. Aqui mesmo ele já atribui esse novo time ao arquivo
            database[index] = temp.copy()
            # Retorno da função, quebrando o looping
            return


# Função que serve para excluir UM time em específico, então pode ficar tranquilo ao utilizá-la. Ela NÃO APAGA O ARQUIVO INTEIRO.
def excluir(database):
    print('\033[31mDigite 999 para cancelar\033[m')
    id = int(input('Digite o ID do time que deseja excluir: '))
    # Verifica se o valor inserido foi '999', para cancelar o processo.
    if id == 999:
        return
    # Cria um looping, levando em consideração o tamanho do arquivo inserido
    for item in range(len(database)):
        # Verifica se o "item/dado/index" é maior ou igual ao time que será retirada. Motivo? Apenas esses realmente importam, visto que será necessário uma reorganização completa de todos os valores APÓS o time retirada, mas não ANTERIOR à posição dele. 
        # TODOS OS VALORES COM INDEX INFERIOR AO TIME A SER RETIRADO, SE MANTERÃO IGUAIS, E TODOS MAIORES QUE ELE, SERÃO ATUALIZADOS.
        if item >= id:
            # Verificada se o item que está sendo tratado é o último. Sempre que um index é retirado, os posteriores a ele vão decaindo de posição de index. O problema é que o len do arquivo se mantém o mesmo, e para evitar esse problema, deletamos o último index após mudarmos todos os outros, retirando esse último valor adicional.
            if id == len(database)-1:
                del database[item]
            # A partir de cada index maior que o que será deletado, os index pegaram o valor do próximo e atribuirão a eles mesmos, garantindo esse decaimento.
            else:
                database[item] = database[item+1]


# Essa função foi criada para evitar uma divergencia de valores durante a execução do programa; visto que após executar algumas funções, e depois outras, essas funções executadas posteriormente passavam a utilizar dados desatualizados, anteriores a última função utilizada.
def sincronizar_database(database):
    # Chama a função que transforma os dados passados em dados brutos, e retorna isso para a variável declarada
    dados_brutos = atualizar_banco(database)
    # Essa variável são os novos dados, que são passados para a função de salvar o arquivo, substituindo todos os antigos dados pelos novos
    write('database.txt', dados_brutos)


# Função que verifica se o time passado já está registrado, e evita isso, pedindo um novo nome, ou cancelando, visto que obteve a informação que tal time já está no sistema
def verificar_duplicidade(database, team):
    # Variável declarada. Sobre o nome escolhido, foi proposital. Um contador geiger apita quando há radiação. Essa variável terá praticamente o mesmo objetivo, notificar em caso de alguma mudança.
    geiger = 0
    while True:
        for item in database:
            # Se o time inserido estiver incluido no arquivo passado, a variável "geiger "receberá +1
            if team in database[item]:
                geiger += 1
        # Se a variável "geiger" for igual a 1, isso significa que um outro time já registrado com esse nome foi identificado, solicitando outro nome. Lembrando, ainda há a opção de cancelar o registro, mesmo aqui, basta o usuário inserir o valor indicado "000" -> pois trata-se de uma "string", logo, irá identificar corretamente o uso de 3 zeros seguidos.
        if geiger == 1:
            print('\033[31mEsse time já está registrado! [000 to cancel]\033[m ')
            geiger = 0
            team = input('Team:\033[34m ')
        else:
            # Retorno básico
            return team
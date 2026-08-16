import pandas as pd
import openpyxl

# Esse arquivo contém funções que utilizam manipulação panda, tendo como objetivo exclusivamente duas funções, uma de geração do arquivo excel e outra de exibição dos dados contidos no arquivo passado.


# Função utilizada para criar o excel com base no arquivo passado.
def criarExcel(database):
    # Cria uma variável que irá receber o retorno da função "separar_planilha", e passa o mesmo arquivo recebido na função "criarExcel".
    values = separar_planilha(database)
    # Criação de uma lista vazia
    ranking = []
    # Atribui a essa lista uma função de ranking baseada na quantidade de equipes disponíveis. (Exemplo com 10 equipes sendo passadas: O ranking irá de 1 até 10)
    for items in values[0]:
        ranking.append(items+1)
    # Cria o arquivo no formato pd, sendo o nome as colunas (exemplo: Team), e os dados pertencentes aquela coluna (exemplo: values[1]). Um detalhe importante é que os dados são passados a partir de uma lista, pegando uma quantidade ilimitada de linhas.
    file = pd.DataFrame({'Ranking': ranking,
                        'Team': values[1],
                         'Wins': values[2],
                         'Streak': values[3],
                         'Loses': values[4],
                         'Points': values[5],
                         'Majors': values[6]})
    
    # Pega o arquivo já no formato pd e o torna em excel, automaticamente salvando-o
    file.to_excel('hltv.xlsx', sheet_name='teams_database',index=False)



# Função para mostrar os times registrados e os dados de cada um.
def exibir_teams(database):
    # Chama a função e atribui os dados retornados dela em uma variável
    values = separar_planilha(database)
    # Cria o arquivo no formato pd, sendo o nome as colunas (exemplo: Team), e os dados pertencentes aquela coluna (exemplo: values[1]). Um detalhe importante é que os dados são passados a partir de uma lista, pegando uma quantidade ilimitada de linhas.
    
    file = pd.DataFrame({
        'Team': values[1],
        'Wins': values[2],
        'Streak': values[3],
        'Loses': values[4],
        'Points': values[5],
        'Majors': values[6]})
    
    # Comandos para exibir a tabela inteira de dados. Se essa parte não for inserida, os dados serão limitados, visto que quanto a tabela é muito grande, o python limita a exibição no print para melhor legibilidade
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Exibe o arquivo final já configurado
    print(file)



# Função criada para transformar os dados recebidos como biblioteca, para listas, de forma que funcione quando passado para o gerador de excel em formas de colunas e linhas
def separar_planilha(database):
    # Gera cada lista com o nome dos tipos de dados que serão armazenados ali dentro
    index = []
    names = []
    wins = []
    streak = []
    loses = []
    points = []
    majors = []
    # Cria uma função que vai trabalhar pegando item por item no dicionário passado, e irá aplicar um append dependendo do index do item na lista correspondente
    for item in database:
        index.append(item)
        names.append(database[item][0])
        wins.append(database[item][1])
        streak.append(database[item][2])
        loses.append(database[item][3])
        points.append(database[item][4])
        majors.append(database[item][5])
        # Retorna todas as listas em uma ordem muito específica
    return index,names,wins,streak,loses,points,majors
from files_functions import *
from db_manipulation import *
from funcionalidades import *

# Team - Wins - Streak - Loses - Majors
database = obter_banco('database.txt')
interface(database)

'''
Colocar as funções de sincronização com o banco de dados na parte de Atualizar Time, pois está dando conflito por não estar atualizando em tempo real de execução.

# DICA PARA TESTE DE EXECUÇÃO PLENA:
Registrar uma playoff teste de major
'''
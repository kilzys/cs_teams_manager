from files_functions import *
from db_manipulation import *
from funcionalidades import *
from external_functions import *

database = obter_banco('database.txt')
interface(database)
criarExcel(database)


'''
Atribuir uma opção de geração de arquivo excel para tratamento de dados
'''
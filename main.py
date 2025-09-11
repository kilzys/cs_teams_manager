from files_functions import *
from db_manipulation import *
from funcionalidades import *
from external_functions import *

# Este é o arquivo que deve ser executado para obter a funcionalidade completa do programa.


# Definir o nome do arquivo onde tudo ficará salvo. Lembre-se sempre de acompanhar o nome com um ".txt".
database = obter_banco('database.txt')

# Chama a função onde tudo acontece, passando o arquivo definido no começo.
interface(database)

# Finaliza com a função de gerar um excel a partir das alterações recentes. Também passa o mesmo arquivo definido no começo.
criarExcel(database)


# OBSERVAÇÃO: Todas as funções utilizadas nesse código foram criadas especificamente para o mesmo. Logo, muitas delas podem acabar criando problemas e conflitos senão adaptadas para o novo uso. Por exemplo a função de gerar o arquivo excel, que trabalha com 6 colunas, não aceitando menos nem mais do que isso.
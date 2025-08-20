# Arquivo que tem como objetivo prover duas funções básicas, uma ed obtenção de dados a partir do arquivo passado, e a outra que salva (substituindo o arquivo inteiro) a partir do arquivo passado


# Função que pega os dados salvos no arquivo passado, e retorna dentro de uma variável.
def read(database):
    file = open(database, 'r')
    return file.read()

# Função que pega o arquivo inserido, mais o conteúdo passado, e registra isso tudo no arquivo passado. Atenção,há um detalhe muito claro aqui que deve ser considerado ao utilizar essa função. Ela reescreve todos os dados inseridos anteriormente naquele arquivo, logo, a versão antiga será completamente perdida, e substituida pela nova.
def write(database, content):
    with open(database, 'w+') as file:
        file.write(content)
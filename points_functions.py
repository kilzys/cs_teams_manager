# Arquivo exclusivamente destinado à atribuição de pontos


# Pede 3 parametros, a arquivo, o id do time que será modificado e um True or False. Se o True for passado, será considerado que o time ganhou, senão, que o time perdeu.
def points(database, id, win=False):
    # Obtemos o streak do time, vendo que ele soma mais pontos por vitória
    streak = int(database[id][2])
    # Obviamente também obtemos os pontos atuais do time
    points = int(database[id][4])
    if win:
        # São 8 pontos por vitória + o valor da streak do time. A cada vitória a streak do time aumenta em 1. Aqui ambos cálculos são realizados
        points += streak+8
        database[id][2] = streak+1
    else:
        # Por derrota são -5 pontos, além de zerar a streak do time.
        points += -5
        database[id][2] = 0
    database[id][4] = points
    

# Sistema de pontuação especial. Necessita os mesmos parâmetros da função anterior, mudando somente o win para type, pedindo um valor. Valor esse que já foi definido no programa para ficar sincronizado com o tipo de pontuação especial a ser obtida
def points_especial(database, id, type):
    # Pega os pontos atuais do time e atribui à uma variável
    points = int(database[id][4])
    match type:
        # Vitória nas quartas de uma competição
        case 0:
            points += 8
        # Vitória nas semi finais de uma competição
        case 1:
            points += 12
        # Ganhou um torneio/competição
        case 2:
            points += 20
        # Chegou nas playoffs de um major
        case 3:
            points += 10
        # Vitória nas quartas de major
        case 4:
            points += 15
        # Vitória nas semi-finais de major
        case 5:
            points += 20
        # Ganhou o major
        case 6:
            # Pega o valor anterior das quantidades de majors ganhos, e atribui mais 1. Lembrando de sempre transformar esses dados para "int" antes
            major = int(database[id][5])+1
            points += 30
            database[id][5] = major
    # Independente do time selecionado, após as mudanças de pontos, eles serão atualizados na no arquivo passado
    database[id][4] = points
    
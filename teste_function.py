def verificar_duplicidade(database, team):
    geiger = 0
    while True:
        for item in database:
            if team in database[item]:
                geiger += 1                
        if geiger == 1:
            print('\033[31mEsse time já está registrado! [000 to cancel]\033[m ')
            geiger = 0
            team = input('Team:\033[34m ')
        else:
            return team
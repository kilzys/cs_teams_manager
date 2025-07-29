def read(database):
    file = open(database, 'r')
    return file.read()

def write(database, content):
    with open(database, 'w+') as file:
        file.write(content)
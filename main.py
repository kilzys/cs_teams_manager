from files_functions import *

while True:
    database = read('database.txt')
    print(database)
    adicionar = input(': ')
    if adicionar == '999':
        break
    write('database.txt', adicionar)
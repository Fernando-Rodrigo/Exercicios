from Ex115.lib.interface import *
from time import sleep


while True:
    opcao = menu(['Cadastrar', 'Listar', 'Sair'])
    if opcao == 1:
        cabecalho('Cadastrar')
    elif opcao == 2:
        cabecalho('Listar')
    elif opcao == 3:
        break
    else:
        print('Digite uma opção entre 1 e 3')
    sleep(1)

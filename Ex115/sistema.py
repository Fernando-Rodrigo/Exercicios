from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = './Ex115/cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    cor(2)
    opcao = menu(['Cadastrar', 'Listar', 'Sair'])
    if opcao == 1:
        cabecalho('Cadastrar')
    elif opcao == 2:
        #Leitura de arquivo
        lerArquivo(arq)
    elif opcao == 3:
        cor(11)
        print()
        print(linha())
        print('Volte sempre!')
        print(linha())
        cor(7)
        break
    else:
        cor(4)
        print('Digite uma opção entre 1 e 3')
    sleep(1)

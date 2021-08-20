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
        #Opção para cadastrar uma nova pessoa no arquivo
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 2:
        #Opção para acessar e ler o conteúdo do arquivo
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

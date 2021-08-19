"""Crie um sistema modularizado que permite cadastrar pessoas pelo nome e idade em um arquivo de texto simples. O sistema vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from cadastropessoas import cadastrar, listar

menu = 'MENU DE OPÇÕES'

while True:
    print('--' * len(menu))
    print(' ' * ((len(menu)//2)-1), menu)
    print('--' * len(menu))
    print(' '*3, '1 - Cadastrar pessoa')
    print(' '*3, '2 - Listar cadastro')
    print(' '*3, '3 - Sair')
    print('--' * len(menu))
    opcao = int(input('Qual a opção desejada? '))
    if opcao == 1:
        cadastrar.cadastro()
    if opcao == 2:
        listar.listar()
    if opcao == 3:
        print('Volte sempre!')
        break

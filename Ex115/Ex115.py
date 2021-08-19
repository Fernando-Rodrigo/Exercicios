"""Crie um sistema modularizado que permite cadastrar pessoas pelo nome e idade em um arquivo de texto simples. O sistema vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from cadastropessoas import cadastrar, listar
from ctypes import windll

menu = 'MENU DE OPÇÕES'
std_out_handle = windll.kernel32.GetStdHandle(-11)

while True:
    windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    print('--' * len(menu))
    print(' ' * ((len(menu)//2)-1), menu)
    print('--' * len(menu))
    print(' '*3, '1 - Cadastrar pessoa')
    print(' '*3, '2 - Listar cadastro')
    print(' '*3, '3 - Sair')
    print('--' * len(menu))
    while True:
        try:
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
            opcao = int(input('Qual a opção desejada? '))
            break
        except:
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
            print('Digite um número inteiro')
    if opcao == 1:
        cadastrar.cadastro()
    if opcao == 2:
        listar.listar()
    if opcao == 3:
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 2)
        print('Volte sempre!')
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
        break
    if opcao < 1 or opcao > 3:
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
        print('Escolha um número entre 1 e 3')

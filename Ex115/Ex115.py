"""Crie um sistema modularizado que permite cadastrar pessoas pelo nome e idade em um arquivo de texto simples. O sistema vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from cadastropessoas import cadastrar, listar
from ctypes import windll
from time import sleep


def menuopcoes():
    windll.kernel32.SetConsoleTextAttribute(std_out_handle, 1)
    print('--' * menu)
    print(menutxt.center(80))
    print('--' * menu)
    print(' '*3, '1 - Cadastrar pessoa')
    print(' '*3, '2 - Listar cadastro')
    print(' '*3, '3 - Sair')
    print('--' * menu)


menu = 40
menutxt = 'Menu de opções'
std_out_handle = windll.kernel32.GetStdHandle(-11)

while True:
    menuopcoes()
    while True:
        try:
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 3)
            opcao = int(input('Qual a opção desejada? '))
            break
        except:
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
            print('Digite um número inteiro')
            sleep(1)
            menuopcoes()
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
    sleep(1)

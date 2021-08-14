"""Faça um mini-programa que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: use cores."""

from sys import stdout
from ctypes import windll

cortexto = []

def cor(texto, cornum):
    std_out_handle = windll.kernel32.GetStdHandle(-11)
    for i in range(0, len(cortexto)):
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, cortexto[i])
        stdout.write(texto)
    # cor padrão é 7, white
    windll.kernel32.SetConsoleTextAttribute(std_out_handle, cornum)


def titulo(msg='', cortexto=7):
    titulo = msg
    tamanho = len(msg) + 6
    numerocor = cortexto
    cor(titulo, numerocor)
    print()
    print('-' * tamanho)
    print('  ', titulo)
    print('-' * tamanho)
    print()


def ajuda(comando):
    cor(msg, 5)
    help(comando)


while True:
    msg='AJUDA INTERATIVA DO PYTHON'
    titulo(msg, 2)
    cmd = str(input('Qual é o comando que deseja ver o manual? (FIM para encerrar) '))
    if cmd in 'FIMFimfim':
        msg = 'VOLTE SEMPRE'
        titulo(msg, 4)
        cor(msg, 7)
        break
    ajuda(cmd)

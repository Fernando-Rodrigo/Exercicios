"""Reescreva a função leiaInt() do desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

from sys import stdout
from ctypes import windll

def leiaInt(num=0):
    valor = 0
    validade = False
    color = [4]
    texto = 'Você deve digitar somente número inteiro'
    std_out_handle = windll.kernel32.GetStdHandle(-11)
    while True:
        try:
            valor = int(input(num))
            validade = True
        except:
            for i in range(0, len(color)):
                windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
                stdout.write(texto)
                print('')
            # cor padrão é 7, white
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
        if validade == True:
            break
    return valor


def leiaFloat(num):
    valor = 0
    validade = False
    color = [4]
    texto = 'Você deve digitar somente número de ponto flutuante'
    std_out_handle = windll.kernel32.GetStdHandle(-11)
    while True:
        try:
            valor = float(input(num).replace(',', '.'))
            validade = True
        except:
            for i in range(0, len(color)):
                windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
                stdout.write(texto)
                print('')
            # cor padrão é 7, white
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
        if validade == True:
            break
    return valor


numInt = leiaInt('Digite um número inteiro: ')

print(f'Você digitou o número {numInt}')

numFloat = leiaFloat('Digite um número decimal: ')

print(f'Você digitou o número flutuante {numFloat :.2f}'.replace('.', ','))

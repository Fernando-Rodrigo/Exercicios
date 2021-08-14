"""Faça um programa que tenha uma função leiaInt() que vai funcionar de maneira semelhante ao input()do Python, so que fazendo a validação para aceitar apenas valor numérico. Ex: n=leiaInt('Digite um n')"""

def leiaInt(num):
    from sys import stdout
    from ctypes import windll
    # -*- coding: utf-8 -*-
    """
    0 = Black          1 = Blue            2 = Green
    3 = Aqua           4 = Red             5 = Purple
    6 = Yellow         7 = White           8 = Gray
    9 = Light Blue     10 = Light Green    11 = Light Aqua
    12 = Light Red     13 = Light Purple   14 = Light Yellow

    Este código é baseado no software Python Wikipedia Bot, distribuído pela MIT license.

    """
    validade = False
    valor = 0
    color = [4]
    texto = 'Você deve digitar somente números inteiros'
    std_out_handle = windll.kernel32.GetStdHandle(-11)
    while True:
        valor = str(input(num))
        if valor.isnumeric():
            valor = int(valor)
            validade = True
        else:
            for i in range(0, len(color)):
                windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
                stdout.write(texto)
                print('')
            # cor padrão é 7, white
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
        if validade:
            break
    return valor



num = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {num}')

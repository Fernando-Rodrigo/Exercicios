"""Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo e realize a contagem. o seu programa tem que realizar três contagens através da função criada: A) de 1 até 10, de 1 em 1 B)de 10 até 0, de 2 em 2 C) Uma contagem personalizada(o programa deve pedir os parâmetros, permitindo aumentar a contagem, diminuir a contagem, funcionar com número negativo e com passo 0, fazer comque seja 1.)."""

from time import sleep

def contador(inicio, fim, passo):
    print()
    print('--' * 30)
    for i in range(inicio, fim, passo):
        print(i)
        sleep(0.75)
    print()
    if fim > inicio or passo < 0:
        print()
        print('--' * 30)
        for i in range(inicio, fim, -passo):
            print(i)
            sleep(0.75)
        print()



contador(1, 10, 1)
contador(10, 0, -2)

i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))

if p == 0:
    contador(i, f, 1)
    if f < i:
        contador(i, f, -1)
else:
    contador(i, f, p)

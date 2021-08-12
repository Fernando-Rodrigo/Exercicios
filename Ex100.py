"""Faça um programa que tenha uma lista  chamada numeros e duas funções chamadas sorteio() e numeroPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma de todos os números pares sorteados pela função anterior. Mostrar os números sorteados, também."""

from random import randint

valores = []

def sorteio():
    for i in range(0,5):
        valores.append(int(randint(0, 10)))
    numeroPar(valores)


def numeroPar(v):
    s = 0
    for i in range(0, 5):
        if v[i]%2 == 0:
            s += v[i]
    print(f'Os valores sorteados foram {v}')
    print(f'A soma dos números pares é {s}')


sorteio()

"""Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da prograssão usando a estrutura while."""

a1 = int(input('Digite o primeiro termo da progreção aritmética: '))
s = int(input('Digite a razão da progreção: '))

pa = a1

c = 0

while c < 10:
    pa += s
    print('O termo {} da PA é {}'.format(c + 1, pa))
    c += 1

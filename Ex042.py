"""Refaça o exercicio 35 dos triângulos, acrecentando o recurso de mostra que triângulo será formado:
-Equilátero: todos os lados iguais;
-Isóceles: dois lados iguais;
-Escaleno: todos os lados diferentes."""

from math import fabs

r1 = float(input('Digite o valor da reta 1 '))
r2 = float(input('Digite o valor da reta 2 '))
r3 = float(input('Digite o valor da reta 3 '))

if fabs(r2 - r3) < r1 < r2 + r3:
    print('As retas formam um triângulo.')
    if r1 == r2 == r3: # Forma de condição alternativa para r1 == r2 and r2 == r3 que mostra o mesmo resultado
        print('O triângulo formado é equilátero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triângulo formado é escaleno.')
    else:
        print('O triângulo formado é isóceles.')
else:
    print('As retas não formam um triângulo.')

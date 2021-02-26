"""Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

n = int(input('Digite um número para calcular a tabuada: '))

for i in range(1, 11):
    print('O valor de {} x {} é {}'.format(n, i, n * i))

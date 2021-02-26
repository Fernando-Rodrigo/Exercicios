"""Faça um programa que clcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500."""

soma = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        soma += i

print('A soma dos números ímpares mútliplos de 3 é {}.'.format(soma))

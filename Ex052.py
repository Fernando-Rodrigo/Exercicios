"""Faça um programa que leia um número inteiro e digita se ele é ou não um número primo."""

resultado = 0

n = int(input('Digite um valor: '))

for i in range (1, n +1):
    if n % i == 0:
        resultado += 1

if resultado == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))

"""Faça um programa que leia um número qualquer e mostre o seu fatorial. """

numero = int(input('Digite um valor para ser calculado o fatorial '))
n = 1
fatorial = 1

while n < numero + 1:
    fatorial = fatorial * n
    n += 1

print('O fatorial do número {} é {}'.format(numero, fatorial))

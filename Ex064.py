"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e a soma entre eles (desconciderando o flag)."""

n = int(input('Entre um número inteiro: (Para parar, digite 999) '))
cont = 0
soma = 0

while n != 999:
    if n != 999:
        cont += 1
        soma += n
    n = int(input('Entre um número inteiro: (Para parar, digite 999) '))

print('Foram digitados {} números e a soma entre eles é {}.'.format(cont, soma))

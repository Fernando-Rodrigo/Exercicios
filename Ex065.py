"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média de todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

num = int(input('Digite um número: '))

maior = menor = num

cont = 's'
soma = 0

while cont != 'n':
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    num = int(input('Digite um novo número: '))
    cont = str(input('Deseja continuar? [s/n]')).lower()

if num > maior:
    maior = num
if num < menor:
    menor = num
soma += num

print('O maior número digitado é {},\no menor número digitado é {}\ne a soma entre eles é {}.'.format(maior, menor, soma))

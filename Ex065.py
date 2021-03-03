"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média de todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

cont = 's'
soma = media = c = maior = menor = 0

while cont != 'n':
    num = int(input('Digite um número: '))
    c += 1
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    cont = str(input('Deseja continuar? [s/n]')).lower()

media = soma / c

print('===' * 10)
print('O maior número digitado é {}.'.format(maior))
print('O menor número digitado é {}.'.format(menor))
print('Foram digitados {} e a média entre eles é {}.'.format(c, media))

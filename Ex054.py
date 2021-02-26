"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

maior = 0
menor = 0

ano = date.today().year

for i in range(1,8):
    anonascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    idade = ano - anonascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Tem {} pessoas que já são maiores e tem {} pessoas que ainda são menores.'.format(maior, menor))

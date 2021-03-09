"""Crie um programa que simule um caixa eletrônico. No início, pergunte ao usuário qual será o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: considere que o caixa tenha notas de R$50, R$20, R$10 e R$1."""

from math import floor

valor = int(input('Qual é o valor que deseja sacar? R$'))

valor50 = valor20 = valor10 = valor1 = resto = 0

while True:
    valor50 = floor(valor / 50)
    resto = valor % 50
    valor20 = floor(resto / 20)
    resto = resto % 20
    valor10 = floor(resto / 10)
    valor1 = resto % 10
    break

print(f'A quantidade de notas de R$50,00 é {valor50}.')
print(f'A quantidade de notas de R$20,00 é {valor20}.')
print(f'A quantidade de notas de R$10,00 é {valor10}.')
print(f'A quantidade de notas de R$1,00 é {valor1}.')

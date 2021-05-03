"""Crie um programa que vá gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o mair valor que estão na tupla."""

from random import randint

num = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

print(f'Os números gerados são: {num}')
print(f'O maior número da tupla é: {max(num)}')
print(f'O menor número da tupla é: {min(num)}')

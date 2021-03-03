"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valore 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = input('Digite o sexo de uma pessoa [M/F]: ').upper()

while sexo not in 'MF':
    sexo = input('Digite corretamente o sexo da pessoa!!! Digite o sexo de uma pessoa [M/F]: ').upper()
print('Você digitou corretamente o sexo!')

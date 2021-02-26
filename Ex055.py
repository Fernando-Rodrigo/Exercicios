"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

pesomenor = 0
pesomaior = 0

for i in range(1,6):
    peso = float(input('Digite o peso da pessoa: '))
    if i == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso < pesomenor:
            pesomenor = peso
        elif peso > pesomaior:
            pesomaior = peso

print('O menor peso digitado foi {}kg e o maior peso digitado foi {}kg.'.format(pesomenor, pesomaior))

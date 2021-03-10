"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$1000,00. C) Qual o nome do produto mais barato."""

total = quant1000 = menorpreco = c = 0
nomem = ' '

while True:
    nome = str(input('Qual é o nome do produto? '))
    preco = float(input('Qual é o preço do produto? R$'))
    c += 1
    
    cont = ' '
    
    while cont not in 'SN':
        cont = str(input('Deseja continuar cadastrando produtos? [S/N] ')).upper().strip()[0]
    
    total += preco

    if preco > 1000:
        quant1000 += 1
    if c == 1 or preco < menorpreco:
        menorpreco = preco
        nomem = nome
    if cont == 'N':
        break

print(f'O valor total da compra é de R${total :.2f}')
print(f'Foram cadastrados {quant1000} produtos que custam mais de R$1000.00')
print(f'O produto mais barato é {nomem} que custa R${menorpreco :.2f}')

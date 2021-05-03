"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final mostre a listagem de preços, organizando os dados em forma tabular."""

lista = ('Caixa', 20, 'Papel', 2, 'Lápis', 1.5, 'Sapato', 300, 'Tênis', 450.76, 'Lanterna', 35.6, 'Mesa', 234)

for i in range (0, len(lista), 2):
    print(f'{lista[i]:.<30} R${lista[i + 1]:>10.2f}')

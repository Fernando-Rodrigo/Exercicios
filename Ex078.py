"""Faça um programa que leia 5 valores numéricos e guarde numa lista. No final mostre qual foi o maior e o menor valor digitados na lista e suas respectivas posições na lista."""

valores = []

for i in range (0,5):
    valores.append(int(input(f'Digite o {i + 1}º valor: ')))

print(f'O maior valor da lista é {max(valores)} e está na posição {valores.index(max(valores)) + 1} da lista.')
print(f'O menor valor da lista é {min(valores)} e está na posição {valores.index(min(valores)) + 1} da lista.')

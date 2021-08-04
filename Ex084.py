"""Faça um programa que leia o peso de várias pessoas, guardando tudo em uma lista. No final mostre: A) Quantas pessoas forma cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves."""
sair = ''

contador = maior = menor = 0
pesolista = []
peso = []

while True:
    peso.append(str(input('Qual é o nome da pessoa? ')))
    peso.append(float(input('Qual é o peso da pessoa? ')))
    if len(pesolista) == 0:
        maoir = menor = peso[1]
    else:
        if peso[1] > maior:
            maior = peso[1]
        elif peso[1] < menor:
            menor = peso[1]
    pesolista.append(peso[:])
    peso.clear()
    contador += 1
    sair = str(input('Deseja continar? [s/n] ')).lower().strip()
    if sair == 'n':
        break

print(f'Foram cadastradas {contador} pessoas.')

print(f'O menor peso encontrado é {menor} e as pessoas com o menor peso são: ', end='')

for p in pesolista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')

print(f'\nO maior peso encontrado é {maior} e as pessoas com o mair peso são: ', end='')

for p in pesolista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()

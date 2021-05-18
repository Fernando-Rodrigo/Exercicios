"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

valores = []
pares = []
impares = []
continuar = ''

while True:
    valores.append(int(input('Entre um valor: ')))
    continuar = str(input('Deseja continuar? [s/n] '))
    if continuar == 'n':
        break

for i in range (0, len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    elif valores[i] % 2 != 0:
        impares.append(valores[i])

print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')

"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente."""

valores = [[], []]

for i in range(0,7):
    num = int(input(f'Digite o {i + 1}º número: '))
    if num % 2 == 0:
        valores[0].append(num)
    elif num % 2 != 0:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()

print(f'Os números pares digitados são {valores[0]}')
print(f'Os números impares digitados são {valores[1]}')

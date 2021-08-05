"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente."""

impares = []
pares = []
valores = [impares, pares]

for i in range(0,7):
    num = int(input(f'Digite o {i + 1}° número: '))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)

pares.sort()
impares.sort()

print(f'Os números pares digitados são {pares}')
print(f'Os números impares digitados são {impares}')
print(f'A lista completa com os núeros pares digitdos é {valores[1]} e impares é {valores[0]}')

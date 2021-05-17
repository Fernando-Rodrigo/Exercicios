"""Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem o sort()). No final mostre a lista ordenanda na tela."""

valores = []
num = 0

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0:
        valores.append(num)
    else:
        if num < valores[i - 1]:
            valores.insert(i - 1, num)
        else:
            valores.append(num)

print(valores)

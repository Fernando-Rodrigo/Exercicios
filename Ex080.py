"""Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem o sort()). No final mostre a lista ordenanda na tela."""

valores = []

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
    else:
        for pos in range(0, 5):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break

print(f'Os valores digitados foram {valores}')

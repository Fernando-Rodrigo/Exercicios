"""Crie um programa que crie uma matriz de 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta."""

matriz = [[], [], []]

for i in range(0, 9):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if i < 3:
        matriz[0].append(valor)
    elif i < 6:
        matriz[1].append(valor)
    elif i < 9:
        matriz[2].append(valor)

print()
print('--' * 30)
print(f'{matriz[0][0], matriz[0][1], matriz[0][2]}')
print(f'{matriz[1][0], matriz[1][1], matriz[1][2]}')
print(f'{matriz[2][0], matriz[2][1], matriz[2][2]}')
print('--' * 30)

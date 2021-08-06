"""Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha."""

matriz = [[], [], []]
somapares = maiorvalor = 0

for i in range(0, 9):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if i < 3:
        matriz[0].append(valor)
    elif i < 6:
        matriz[1].append(valor)
    elif i < 9:
        matriz[2].append(valor)

for j in range(0,3):
    if matriz[1][j] > maiorvalor:
        maiorvalor = matriz[1][j]
    for k in range(0,3):
        if matriz[j][k]%2 == 0:
            somapares += matriz[j][k]

print(f'A soma dos valores pares digitados é {somapares}')
print(f'A somados valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {maiorvalor}')

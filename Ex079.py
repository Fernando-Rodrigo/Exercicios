"""Crie um programa onde o usuário digita vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem crescente."""

valores = []
continuar = ''

while True:
    if continuar == 'n':
          break
    else:
        num = int(input('Digite um número: '))
        if num not in valores:
            valores.append(num)
        else:
            print('O valor já foi adicionado a lista!!!')
    continuar = str(input('Deseja continuar? [s/n] ')).lower().strip()

valores.sort()
print(f'Os valores digitados foram {valores}')

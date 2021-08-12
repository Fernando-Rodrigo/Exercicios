"""Faça um programa que tenha uma função chamada maior(), que receba vários parãmetros com valores inteiros. Seu programa deve anlisar todos os valores e dizer qual deles é o maior. Informar a quantidade de números passados como parâmetros."""

valores = []
cont = ''

def maior(v):
    print()
    print('--' * 30)
    print(f'Os valores digitados foram {v}')
    print(f'O total de valores digitados foi {len(v)}')
    print(f'O maior valor digitado foi {max(v)}')
    print('--' * 30)


while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if cont in 'SsNn':
            break
        print('Escolha somente sim ou não')
    if cont == 'N':
        break

maior(valores)

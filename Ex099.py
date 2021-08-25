"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa deve anlisar todos os valores e dizer qual deles é o maior. Informar a quantidade de números passados como parâmetros."""

def maior(* v):
    print()
    print('--' * 30)
    print(f'Os valores digitados foram {v}')
    print(f'O total de valores digitados foi {len(v)}')
    print(f'O maior valor digitado foi {max(v)}')
    print('--' * 30)


maior(0, 9, 7, 3, 5)
maior(6)
maior(99, 104, 3, 200, 1, 25, 73, 88, 99, 111)

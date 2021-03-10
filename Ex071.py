"""Crie um programa que simule um caixa eletrônico. No início, pergunte ao usuário qual será o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: considere que o caixa tenha notas de R$50, R$20, R$10 e R$1."""

valor = int(input('Qual é o valor que deseja sacar? R$'))

cedula = 50
total = 0

while True:
    if valor >= cedula:
        total += 1
        valor -= cedula
    else:
        if total >= 1:
            print(f'A quantidade de notas de {cedula} é {total}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula =1
        total = 0
        if valor == 0:
            break

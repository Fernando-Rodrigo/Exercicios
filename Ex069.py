"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos."""

Cont18 = ContHomens = Cont20 = 0

while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o sexo da pessoa? [M/F] ')).upper().strip()[0]
    idade = int(input('Qual é a idade da pessoa cadastrada? '))
    while idade < 0:
          idade = int(input('Qual é a idade da pessoa cadastrada? '))
    cont = ' '
    while cont not in 'NS':
        cont = str(input('Deseja continuar a cadastrar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        Cont18 += 1
    if sexo == 'M':
        ContHomens += 1
    if sexo == 'F' and idade < 20:
        Cont20 += 1
    if cont == 'N':
        break


print(f'Foram cadastradas {Cont18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {ContHomens} homens.')
print(f'Foram cadastradas {Cont20} mulheres com menos de 20 anos.')

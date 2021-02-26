"""Crie um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com a média atingida:
-média abaixo de 5.0: reprovado
-média entre 5 e 6.9: recuperação
-média igual ou superior: aprovado."""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Reprovado!')
elif media <= 6.9:
    print('Recuperação!')
elif media >= 7:
    print('Aprovado!')

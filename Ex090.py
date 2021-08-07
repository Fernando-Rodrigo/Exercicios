"""Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final mostre, mostre o conteúdo da estrutura na tela. Fazer para um único aluno e usar a nota 7 como referência mínima para aprovção."""

aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recupeação'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'

print(f'O aluno {aluno["nome"]} teve de média {aluno["media"]} e a situação é {aluno["situacao"]}.')

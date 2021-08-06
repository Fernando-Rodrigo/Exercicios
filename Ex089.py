"""Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário mostre as notas de cada aluno individualmente."""

notas = [[], [], []]
sair = aluno = opcao = ''
indice = 0


while True:
    notas[0].append(str(input('Digite o nome do aluno ')))
    notas[1].append(float(input('Digite a primeira nota: ')))
    notas[2].append(float(input('Digite a segunda nota: ')))
    sair = str(input('Deseja sair? [s/n] ')).lower().strip()
    if sair == 's':
        break

for c in range(0,len(notas[0])):
    print(f'A média do aluno {notas[0][c]} é {(notas[1][c] + notas[2][c]) / 2}')

opcao = str(input('Deseja ver as notas do aluno? [s/n] ')).lower().strip()
if opcao == 's':
    while True:
        aluno = str(input('Qual é o nome do aluno que deseja ver as notas? '))
        if aluno in notas[0]:
            indice = notas[0].index(aluno)
        else:
            print('Aluno não encontrado na lista!!')
        print(f'As notas do {aluno} são {notas[1][indice]} e {notas[2][indice]}.')
        sair = str(input('Deseja consultar mais notas? [s/n] ')).lower().strip()
        if sair == 'n':
            print('Obrigado pela presença!!')
            break
else:
    print('Obrigado pela presença!!')

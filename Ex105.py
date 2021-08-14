"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar e vai retornar um dicionário com as seguntes informações: -Qauntidade de notas; -A maior nota; -A menor nota; -A média da turma; -A situção(opcional(padrão=False)). Adicione também as docstrings da função. Passar várias notas por padrão sem pedir ao usuário para digitar as notas e situação."""

def notas(*notas, situacao=False):
    media = sum(notas) / len(notas)
    if situacao == True:
        if media < 4:
            print(f'A maior nota é {max(notas)}, a menor nota é {min(notas)} e a média é {media :.2f} e a situação é Péssima')
        if media < 5:
            print(f'A maior nota é {max(notas)}, a menor nota é {min(notas)} e a média é {media :.2f} e a situação é Ruim')
        if media < 7:
            print(f'A maior nota é {max(notas)}, a menor nota é {min(notas)} e a média é {media :.2f} e a situação é Boa')
        if media < 9:
            print(f'A maior nota é {max(notas)}, a menor nota é {min(notas)} e a média é {media :.2f} e a situação é Muito Boa')
        if media >= 9:
            print(f'A maior nota é {max(notas)}, a menor nota é {min(notas)} e a média é {media :.2f} e a situação é Excelente')
    else:
        print(f'A maior nota é {max(notas)}, a menor nota é {min(notas)} e a média é {media :.2f}')


notas(1, 7, 8.5, 6, situacao=False)
notas(9, 7, 9.1, 8.9, 7.8, 7.9, 6, 8, situacao=True)

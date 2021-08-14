"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar e vai retornar um dicionário com as seguntes informações: -Qauntidade de notas; -A maior nota; -A menor nota; -A média da turma; -A situção(opcional(padrão=False)). Adicione também as docstrings da função. Passar várias notas por padrão sem pedir ao usuário para digitar as notas e situação."""

def notas(*notas, situacao=False):
    """
    ->Função de análise de notas de uma turma
    :param *notas: recebe várias notas para serem analisadas
    :param situação: recebe True ou False para mostrar ou não a situação da sala
    :return: retorna um dicionário com as informações das notas recebidas
    """

    nota = {}
    
    media = sum(notas) / len(notas)
    nota['Total'] = len(notas)
    nota['MaiorNota'] = max(notas)
    nota['MenorNota'] = min(notas)
    nota['Média'] = media

    if situacao == True:
        if media < 4:
             nota['situação'] = 'Péssima'
        if media < 5:
            nota['situação'] = 'Ruim'
        if media < 7:
            nota['situação'] = 'Boa'
        if media < 9:
            nota['situação'] = 'Muito Boa'
        if media >= 9:
            nota['situação'] = 'Excelente'

    return nota


print(notas(1, 7, 8.5, 6, 2.5, situacao=False))
print(notas(9, 7, 9.1, 8.9, 7.8, 7.9, 6, 8, situacao=True))

"""Crie um programa que leia o nome, ano de nascimento, e carteira de trabalho cadastre-os(com idade) em um dicionário e se por caso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Fazer somente para uma pessoa e considerar 35 anos de contribuição para aposentadoria."""

from datetime import date

trabalhador = {}
datatemp = 0

trabalhador['nome'] = str(input('Digite o nome do trabalhador: '))
trabalhador['idade'] = date.today().year - int(input('Digite a idade do trablhador: '))
trabalhador['carteira'] = int(input('Digite o número da carteira de trablho: '))

if trabalhador["carteira"] > 0:
    trabalhador['anoinicio'] = int(input('Digite o ano de contratação: '))
    trabalhador['salario'] = float(input('Digite o salário do trabalhador: R$'))
    datatemp = date.today().year - trabalhador["anoinicio"]
    trabalhador['anoaposentadoria'] = (35 - datatemp) + trabalhador["idade"]
    print(f'O trabalhador {trabalhador["nome"]} de {trabalhador["idade"]} anos, tem a carteira de trabalho de número {trabalhador["carteira"]}.')
    print(f'{trabalhador["nome"]} vai se aposentar com {trabalhador["anoaposentadoria"]} anos.')
    print(f'O salário atual é de R${trabalhador["salario"] :.2f}')
elif trabalhador["carteira"] == 0:
    print(f'{trabalhador["nome"]} de {trabalhador["idade"]} anos, tem a carteira de trabalho de número {trabalhador["carteira"]} e ainda não contribuiu com a previdência.')

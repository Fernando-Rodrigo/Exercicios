"""Faça um programa qe tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome do jogador(padrão= <desconhecido>) e quantos gols ele marcou(padrão=0 gol(s) marcados). O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nãotenha sido informado corretamente."""

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} no campeonato.')

nome = str(input('Qual é o nome do jogador? '))
gols = str(input('Quantos gols o jogador fez na temporada? '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)

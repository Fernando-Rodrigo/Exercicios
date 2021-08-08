"""Crie um programa onde 4 jogadores joguem um dado e tenhamum resultado aleatório. Guarde esses resultados em um dicionário. No final coloque esse dicionário em oredem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
from operator import itemgetter

dados = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)} 
rank = {}

for k,v in dados.items():
    print(f'O {k} obteve {v} no dado.')
    sleep(0.75)

#Para ordenar um dicionário, é necessário importar o itemgetter e usar a função sorted como acontece com tuplas para fazer a ordenação dos dados.
rank = sorted(dados.items(), key=itemgetter(1), reverse=True)

print()
print('--' * 30)
print('  Ranking dos jogadores  ')

"""Uma vez ordenado os dados, para exibir é necessário usar a opção enumarete para acessar os dados do 
dicionário para exibir cada item de maneira separada e organizada."""
for k,v in enumerate(rank):
    print(f'O jogador {v[0]} ficou em {k + 1}º com o número {v[1]}')
    sleep(0.75)

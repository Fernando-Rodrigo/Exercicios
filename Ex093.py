"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será gardado em um dicionário, incluindo o total de gols no campeonato. Fazer isso para um jogador apenas."""

jogador = {}
temp = []

jogador['nome'] = str(input('Digite o nome do jodador: '))
partidas = int(input('Digite quantas partidas o jogador participou: '))

for c in range(0, partidas):
    temp.append(int(input(f'Digite gols fez na partida {c + 1}: ')))

jogador['gols'] = temp[:]
jogador['total'] = sum(temp)

print()
print('--' * 30)
print(jogador)

print()
print('--' * 30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print()
print('--' * 30)
print(f'O jogador {jogador["nome"]} participou de {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'Na partida {i + 1} o jodador fez {v} gols')
print(f'O saldo de gols da temporada é {jogador["total"]}')

"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será gardado em um dicionário, incluindo o total de gols no campeonato. Fazer isso para um jogador apenas."""

jogador = {}
totalgols = 0

jogador['nome'] = str(input('Digite o nome do jodador: '))
jogador['partidas'] = int(input('Digite quantas partidas o jogador participou: '))

for i in range(0,jogador["partidas"]):
    jogador[f'gols{i}'] = int(input(f'Digite gols fez na partida {i + 1}: '))
    totalgols += jogador[f'gols{i}']

jogador['total'] = totalgols

print()
print('--' * 30)
print(f'O jogador {jogador["nome"]} participou de {jogador["partidas"]} partidas.')
for i in range(0,jogador["partidas"]):
    print(f'Na partida {i + 1} o jodador fez {jogador[f"gols{i}"]} gols')
print(f'O saldo de gols da temporada é {jogador["total"]}')

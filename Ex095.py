"""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, inclindo um sistema de visualização de detalhes do aproveitamento de cada jogador. Colocar mensagem de erro para o caso de solicitação de dados de jogador não cadastrado no programa."""

jogador = {}
listajogadores = []
temp = []
cont = ''

while True: 
    jogador['nome'] = str(input('Digite o nome do jodador: '))
    partidas = int(input('Digite quantas partidas o jogador participou: '))

    for c in range(0, partidas):
        temp.append(int(input(f'Digite gols fez na partida {c + 1}: ')))

    jogador['gols'] = temp[:]
    jogador['total'] = sum(temp)
    temp.clear()
    listajogadores.append(jogador.copy())
    jogador.clear()
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if cont in 'NnSs':
            break
        print('Escolha sim ou não')
    if cont == 'N':
        break

print()
print('--' * 30)
for j in listajogadores:
    print(f'O jogador {j["nome"]} participou de {len(j["gols"])} jogos e fez {j["total"]} gols no total')

while True:
    nome = str(input('Qual jogador deseja ver o desempenho? '))
    if nome == j["nome"]:
        print(f'O jogador {j["nome"]} participou de {len(j["gols"])} partidas.')
        for i, v in enumerate(j["gols"]):
            print(f'Na partida {i + 1} o jodador fez {v} gols')
        print(f'O saldo de gols da temporada é {j["total"]}')
    while True:
        cont = str(input('Deseja ver detalhes de um jogador? [S/N] ')).upper().strip()[0]
        if cont in 'NnSs':
            break
        print('Escolha sim ou não')
    if cont == 'N':
        break

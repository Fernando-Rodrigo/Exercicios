"""Crie uma tupla preenchida com os 20 primeiros colocados do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Apenas os 5 primeiros colocados. b) Os últimos 4 colocados da tabela. c) Uma lista com os times em ordem alfabética. d) Em que posição está o time da Chapecoense."""

times = ('Flamengo', 'Internacional', 'Atlétivo-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

print('Os cinco primeiros colocados da tabela são:')
for i in range(0,5):
    print(f'    {i + 1}º {times[i]}')

print('Os quatro ultimos colocados da tabela são:')
for i in range(16,20):
    print(f'    {i + 1}º {times[i]}')

print(f'Os times da lista ordenados em ordem alfabética é {sorted(times)}')

print(f'O time do São Paulo está em {times.index("São Paulo") + 1}ª posição.')

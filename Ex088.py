"""Faça um programa que ajude um jogador da mega sena a criar palpites. O programa ira perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada número cadastrado em uma lista composta."""

from random import randint

megasena = []
temp = []
numerosorteado = jogos = 0

jogos = int(input('Quantos jogos deseja fazer? '))


for c in range(0, jogos):
    for i in range(0,6):
        numerosorteado = int(randint(1,60))
        if numerosorteado not in temp:
            temp.append(numerosorteado)
        else:
            numerosorteado = int(randint(1,60))
            temp.append(numerosorteado)
        temp.sort()
    megasena.append(temp[:])
    temp.clear()

print('Os jogos feitos estão listados abaixo')
for c in range(0, jogos):
    print(f'{c + 1}º jogo {megasena[c]}')

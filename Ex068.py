"""Faça um programa que joge par ou ímpar com o computador. O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

cont = 0

while True:
    NumComp = int(randint(1,10))
    NumJogador = int(input('Digite um valor: '))
    ParImpar = str(input('Par ou ímpar? [p/i]')).lower().strip()[0]
    parjogador = NumJogador % 2
    
    if ParImpar == 'p':
        if NumJogador > NumComp and parjogador == 0:
            print('Você ganhou essa partida!!!')
            cont += 1
        else:
            print('Você perdeu!!!')
            break
    else:
        if NumJogador > NumComp and parjogador != 0:
            print('Você ganhou essa partida!!!')
            cont += 1
        else:
            print('Você perdeu!!!')
            break

print(f'O jogo acabou e você venceu {cont} vezes.')

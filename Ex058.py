"""Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint

r = int(randint(0, 10))

resultado = False

cont = 0

while not resultado:
    n = int(input('Digite seu palpite: '))
    cont += 1

    if n < r:
        print('Não foi desta vez. Tente um número maior.')
    elif n > r:
        print('Não foi desta vez. Tente um número menor.')
    else:
        resultado = True

print('Parabéns, você acertou o número escolhido! Você tentou {} vezes até acertar.'.format(cont))

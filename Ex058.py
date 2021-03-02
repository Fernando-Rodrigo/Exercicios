"""Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint

n = int(input('Tente adivinhar um número entre 0 e 10: '))
r = int(randint(0, 10))

while n != r:
    print('Não foi desta vez. Tente outra vez.')
    n = int(input('Tente adivinhar um número entre 0 e 10 novamente: '))

print('Parabéns, você acertou o número escolhido!')

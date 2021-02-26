from random import randint

n = int(input('Tente adivinhar um número entre 0 e 5 '))
r = int(randint(0, 5))

if n == r:
    print('Parabéns, você acertou o número!!!')
else:
    print('Não foi desta vez. Tente outra vez.')

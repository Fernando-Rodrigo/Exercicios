"""Crie um programa que faça o computador jogar jokempô com você."""

from random import randint

print('Jokenpô')
opcao = int(input('Escolha 1 para papel\n2 para pedra\n3 para tesoura '))
opcaocomp = int(randint(1, 3))

if (opcao == 1 and opcaocomp == 2) or (opcao == 2 and opcaocomp == 3) or (opcao == 3 and opcaocomp == 1):
    print('Você ganhou!')
elif (opcao == 2 and opcaocomp == 1) or (opcao == 3 and opcaocomp == 2) or (opcao == 1 and opcaocomp == 3):
    print('Você perdeu!')
elif opcao > 3:
    print('Opção inválida! Tente novamente.')
else:
    print('Empataram')

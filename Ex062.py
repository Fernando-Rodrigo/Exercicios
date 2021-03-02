"""Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele quer que mostre 0 termos."""

a1 = int(input('Digite o primeiro termo da progreção aritmética: '))
s = int(input('Digite a razão da progreção: '))

pa = a1

c = 0

while c < 10:
    pa += s
    print('O termo {} da PA é {}'.format(c + 1, pa))
    c += 1

opcao = int(input('Digite [1] para mostrar mais termos ou [0] para encerrar o programa: '))

while opcao != 0:
    pa += s
    print('O termo {} da PA é {}'.format(c + 1, pa))
    opcao = int(input('Digite [1] para mostrar mais termos ou [0] para encerrar o programa: '))

print('Fim do programa!!')

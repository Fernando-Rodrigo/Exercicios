"""Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele quer que mostre 0 termos."""

a1 = int(input('Digite o primeiro termo da progreção aritmética: '))
s = int(input('Digite a razão da progreção: '))

pa = a1

c = 1
opcao = 10
total = 0

while opcao != 0:
    total += opcao
    while c <= total:
        pa += s
        print('O termo {} da PA é {}'.format(c, pa))
        c += 1
    opcao = int(input('Quantos termos a mais você quer que exiba dessa PA? '))


print('===' * 25)
print('A prograssão aritmética tem {} termos!!'.format(total))
print('Fim do programa!!')

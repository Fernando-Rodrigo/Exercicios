"""Escreva um programa que leia um número inteiro qualquer e peça  para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal"""

print('Conversor de bases numéricas.')
numero = int(input('Entre o valor do número: '))
base = int(input('Escolha\n 1 para binário\n 2 para octal\n 3 para hexadecimal\nOpção: '))

if base == 1:
    bin_a = bin(numero)
    print('O número escolhido na base binária é {}.'.format(bin_a[2:]))
elif base == 2:
    oct_a = oct(numero)
    print('O número na base octal é {}.'.format(oct_a[2:]))
elif base == 3:
    hex_a = hex(numero)
    print('O número na base hexadecimal é {}.'.format(hex_a[2:]))
else:
    print('Opção inválida.')

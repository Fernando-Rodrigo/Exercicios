"""Crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando os espaços."""

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
if inverso == junto:
    print('A frase {} é um palindromo.'.format(frase))
else:
    print('A frase {} não é um palindromo.'.format(frase))

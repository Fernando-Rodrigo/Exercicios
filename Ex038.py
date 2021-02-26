"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens:
-o primeiro valor é maior;
-o segundo valor é maior;
-os dois vlores são iguais."""

n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))

if n1 > n2:
    print('O primeiro número {} é o maior.'.format(n1))
elif n2 > n1:
    print('O segundo número {} é o maior.'.format(n2))
else:
    print('Os números digitados são iguais')

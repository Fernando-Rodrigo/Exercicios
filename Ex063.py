"""Escreva um programa que leia um númer n inteiro qualquer e mostre na tela os n primeiros elementos da sequência de Fibonacci. """

n = int(input('Digite um valor de n termos da sequência de Fibonacci: '))
fibo = 0
c = 1
temp1 = 0
temp2 = 1

print ('{}'.format(temp1), end = ' ')

while c < n:
    fibo = temp1 + temp2
    temp2 = temp1
    temp1 = fibo
    print('{}'.format(fibo), end = ' ')
    c += 1

print('\nFim!!')

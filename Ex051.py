"""Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros termos dessa progressão."""

a1 = int(input('Digite o primeiro termo da progreção aritmética: '))
s = int(input('Digite a razão da progreção: '))

pa = a1

for i in range (1, 11):
    pa += s
    print('{}'.format(pa))

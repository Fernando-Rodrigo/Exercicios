"""Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando a flag)."""

soma = cont = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        soma += n
        cont += 1

print(f'Foram digitados {cont} e a soma entre eles é {soma}.')

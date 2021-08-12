"""Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno."""

a = 0

def area(l, c):
    a = l * c
    print()
    print(f'A área do retângulo é de {a}m².')


largura = int(input('Digite a largura de um retângulo(m): '))
comprimento = int(input('Digite o comprimento do retângulo(m): '))
area(largura, comprimento)

"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade(). Faça um programa que importe esse modulo e use alguma dessas funções."""

import moeda

valor = float(input('Digite um valor monetário: R$'))
taxa = float(input('Digite a taxa: '))

print(f'O valor R${valor} com {taxa}% de aumento é R${moeda.aumentar(valor, taxa)}')
print(f'O valor R${valor} com {taxa}% de desconto é R${moeda.diminuir(valor, taxa)}')
print(f'O dobro do valor R${valor} é R${moeda.dobro(valor)}')
print(f'A metade do valor R${valor} é R${moeda.metade(valor)}')

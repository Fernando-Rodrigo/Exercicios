"""Adapte o exercício 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como valor monetário formatado."""

import moeda

valor = float(input('Digite um valor monetário: R$'))

print(f'O valor R${moeda.moeda(valor)} com 20% de aumento é R${moeda.moeda(moeda.aumentar(valor))}')
print(f'O valor R${moeda.moeda(valor)} com 30% de desconto é R${moeda.moeda(moeda.diminuir(valor))}')
print(f'O dobro do valor R${moeda.moeda(valor)} é R${moeda.moeda(moeda.dobro(valor))}')
print(f'A metade do valor R${moeda.moeda(valor)} é R${moeda.moeda(moeda.metade(valor))}')

"""Adapte o exercício 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como valor monetário formatado."""

import moeda

valor = float(input('Digite um valor monetário: R$'))
taxa = float(input('Digite a taxa: '))

print(f'O valor R${moeda.moeda(valor)} com {moeda.moeda(taxa)}% de aumento é R${moeda.moeda(moeda.aumentar(valor, taxa))}')
print(f'O valor R${moeda.moeda(valor)} com {moeda.moeda(taxa)}% de desconto é R${moeda.moeda(moeda.diminuir(valor, taxa))}')
print(f'O dobro do valor R${moeda.moeda(valor)} é R${moeda.moeda(moeda.dobro(valor))}')
print(f'A metade do valor R${moeda.moeda(valor)} é R${moeda.moeda(moeda.metade(valor))}')

"""Adapte o exercício 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como valor monetário formatado."""

import moeda

valor = float(input('Digite um valor monetário: R$'))
taxa = float(input('Digite a taxa: '))

print(f'O valor {moeda.moeda(valor)} com {taxa}% de aumento é {moeda.moeda(moeda.aumentar(valor, taxa))}')
print(f'O valor {moeda.moeda(valor)} com {taxa}% de desconto é {moeda.moeda(moeda.diminuir(valor, taxa))}')
print(f'O dobro do valor {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade do valor {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')

"""Modifique as funções que foram criadas no disafio 107, para que aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

import moeda

valor = float(input('Digite um valor monetário: R$'))
taxa = float(input('Digite a taxa: '))

print(f'O valor R${moeda.moeda(valor)} com {taxa}% de aumento é R${moeda.aumentar(valor, taxa, True)}')
print(f'O valor R${moeda.moeda(valor)} com {taxa}% de desconto é R${moeda.diminuir(valor, taxa, True)}')
print(f'O dobro do valor R${moeda.moeda(valor)} é R${moeda.dobro(valor, True)}')
print(f'A metade do valor R${moeda.moeda(valor)} é R${moeda.metade(valor, True)}')

"""Crie um pacote chamado utilidadeCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108, 109 para o primeiro pacote e mantenha tudo funcionando."""

from utilidadeCeV import moeda

valor = float(input('Digite um valor monetário: R$'))
print(moeda.resumo(valor))

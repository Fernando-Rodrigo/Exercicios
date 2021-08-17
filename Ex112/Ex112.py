"""Dentro do pacote utilidadeCeV que criamos no desafio 111, temos o módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como função input(), mas com a validação de dados, para aceitar apenas valores que sejam monetários."""

import utilidadeCeV

valor = utilidadeCeV.dado.leiaDinheiro('Digite um valor monetário: R$')
taxa = float(input('Digite a taxa: '))

print(utilidadeCeV.moeda.resumo(valor, taxa))

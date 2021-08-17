"""Dentro do pacote utilidadeCeV que criamos no desafio 111, temos o módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como função input(), mas com a validação de dados, para aceitar apenas valores que sejam monetários."""

from utilidadeCeV import dado, moeda

valor = dado.leiaDinheiro('Digite um valor monetário: R$')
taxa = dado.leiaDinheiro('Digite a taxa: ')

moeda.resumo(valor, taxa)

"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto;
-à vista cartão: 5% de desconto;
-em até 2x no cartão: preço normal;
-3x ou mais no cartão: 20% de juros."""

valor = float(input('Digite o valor do produto: R$'))
formapagamento = int(input('Digite 1 para pagamento à vista com dinheiro ou cheque \n2 para pagamento com cartão à vista \n3 para para pagamento em até 2x no cartão \n4 para pagamento em 3x ou mais no cartão '))

if formapagamento == 1:
    valorpagar = valor * 0.9
elif formapagamento == 2:
    valorpagar = valor * 0.95
elif formapagamento == 3:
    valorpagar = valor
elif formapagamento == 4:
    valorpagar = valor + valor * 0.2

print('O preço de {} será no total de R${}.'.format(valor, valorpagar))

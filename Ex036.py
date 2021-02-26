"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não vai poder exceder 30% do salário ou então o empréstimo será negado."""

valorcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos ele vai pagar? '))

parcelas = valorcasa / (anos * 12)
porcentagem = parcelas/salario

if porcentagem <= 0.3:
    print('A compra foi aprovada!')
else:
    print('A compra não foi aprovada!')

print('O valor da casa é {}, o salário é {} e vai pagar em {} anos.'.format(valorcasa, salario, anos))
print('O número de parcelas é {} e a porcentagem do salário é {}.'.format(parcelas, porcentagem))

sal = float(input('Qual é o salário do funcionário? R$'))

if sal <= 1250:
    print('O salário de R${:.2f} foi para R${:.2f} e teve um aumento de R${:.2f}.'.format(sal, sal + sal * 0.15, sal * 0.15))
else:
    print('O salário de R${:.2f} foi para R${:.2f} e teve um aumento de R${:.2f}.'.format(sal, sal + sal * 0.1, sal * 0.1))

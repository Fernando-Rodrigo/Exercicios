sal = float(input('Qual é o salário do funcionário? '))
rea = float(input('Qual é o valor do reajuste? '))

aum = sal + (sal * rea/100)

print('O novo salário com {:.2f}% de aumento é {:.2f}'.format(rea, aum))

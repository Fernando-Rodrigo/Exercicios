pr = float(input('Qual é o preço do produto? '))
des = float(input('Qual é o valor do desconto? '))

prd = pr - (pr * des/100)

print('O valor do produto com o desconto é {:.2f}'.format(prd))

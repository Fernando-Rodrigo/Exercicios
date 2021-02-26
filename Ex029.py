v = float(input('Qual a velocidade do carro? '))

if v <= 80:
    print('Você não foi multado.')
else:
    m = (v - 80) * 7
    print('Você passou do limite de velocidade, recebeu uma multa de R${:.2f} por exceder o limite em {}km.'.format(m, v-80))

cv = int(input('Quantos quilometros você viajou? '))

if cv <= 200:
    p = 0.5 * cv
    print('O valor da passagem é R${:.2f} e o valor por quilometro é R$0.50.'.format(p))
else:
    p = 0.45 * cv
    print('O valor da passagem é R${} e o valor por quilometro é R$0.45'.format(p))

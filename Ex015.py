km = float(input('Quantos quilometros rodou com o carro? '))
d = float(input('Por quantos dias o carro ficou alugado? '))

p = (km * 0.15) + (d * 60)

print('O valor do aluguel do carro por {:.2f} dias alugado e {:.2f}km rodados é: R${:.2f}'.format(d, km, p))

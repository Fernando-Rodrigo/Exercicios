import math

r1 = float(input('Digite o valor da reta 1 '))
r2 = float(input('Digite o valor da reta 2 '))
r3 = float(input('Digite o valor da reta 3 '))

if math.fabs(r2 - r3) < r1 < r2 + r3:
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo.')

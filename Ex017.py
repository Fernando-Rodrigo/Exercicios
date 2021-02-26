import math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))

# math.hypot é um método para calcular a hipotenusa de um triangulo retângulo
# h = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
h = math.hypot(ca, co)

print('O valor da hipotenusa é: {:.2f}'.format(h))

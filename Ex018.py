from math import radians, sin, cos, tan
n = float(input('Digite um ângulo '))
ng = radians(n)

s = sin(ng)
c = cos(ng)
t = tan(ng)

print('O seno é {:.5f}, o cosseno é {:.5f} e a tangente é {:.5f}'.format(s, c, t))

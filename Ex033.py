n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
n3 = int(input('Digite o terceiro número '))

if n1 > n2 and n1 > n3:
    print('O primeiro valor, {}, é o maior.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O segundo valor, {}, é o maior.'.format(n2))
else:
    print('O terceiro valor, {}, é o maior.'.format(n3))

if n1 < n2 and n1 < n3:
    print('O primeiro valor, {}, é o menor.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O segundo valor, {}, é o menor.'.format(n2))
else:
    print('O terceiro valor, {}, é o menor.'.format(n3))

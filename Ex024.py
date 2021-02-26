# coding=utf-8
nome = str(input('Digite o nome da cidade onde mora para saber se tem Santo no nome ')).strip()

u = nome.upper()
n = u.find('SANTO')

if n == 0:
    print('O nome da cidade tem Santo no início.')
else:
    print('O nome da cidade não tem Santo no início.')

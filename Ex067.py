"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O Programa será interrompido quando o número solicitado for negativo."""

while True:
    n = int(input('Digite um número: '))
    print('---' * 10)
    
    if n < 0:
        break
    else:
        for cont in range (1, 11):
            print(f'{n} * {cont} = {(cont * n)}')
    
    print('---' * 10)

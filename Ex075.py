"""Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a) Quantas vezes apareceu o valor 9. b) Em que posição foi digitado o primeiro valor 3. c) Quais foram os números pares."""

numero = 0

num = (int(input('Entre o primeiro valor: ')), int(input('Entre o segundo valor: ')), int(input('Entre o terceiro valor: ')), int(input('Digite o quarto valor: ')))

for i in range (0,4):
    if num[i] % 2 == 0:
        print(f'Numero par: {num[i]}')

if 3 in num:
    print(f'O indice do primeiro 3 é: {num.index(3)}')
else:
    print('O número 3 não apareceu na tupla.')
print(f'Aparece {num.count(9)} vezes o número 9.')

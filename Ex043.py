"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMCe mostre o seu status, de acordo com  tabel a abaixo: 
-Abaixo de 18.5: Abaixo do peso;
-Entre 18.5 e 25: Peso ideal;
-25 até 30: sobrepeso;
-30 até 40: obesidade;
-Acíma de 40: obesidade mórbida."""

from math import pow

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / pow(altura, 2)

print('O valor do IMC é {:.2f}.'.format(imc))

if imc <= 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade mórbida.')

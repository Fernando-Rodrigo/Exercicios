"""Crie um programa que tenha uma tupla totalmente preenchida por uma contegem por extenso, de 0 até 20. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso."""

numero = int(input('Digite um número inteiro entre 0 e 20: '))

numeroext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print(f'O número {numero} por extenso é {numeroext[numero]}.')

"""Crie um programa que vai ler vários números e vai colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada em ordem decrescente. C) Se o 5 foi digitado e está ou não na lista."""

valores = []
continuar = ''

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [s/n] ')).strip().lower()
    if continuar == 'n':
        break

if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')

valores.sort(reverse = True)
print(f'O tamanho da lista é {len(valores)}')
print(f'A lista ordenada em ordem decrescente fica {valores}')

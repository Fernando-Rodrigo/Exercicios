"""Faça um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional = False) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

from time import sleep

def fatorial(num = 1, show = False):
    """
    ->Função para calcular o fatorial de um número, mostrar o resultado e caso tenha sido solicitado, mostrar o processo de cálculo do fatorial.
    :param num: recebe o número escolhido para o calculo do fatorial
    :param show: recebe True se foi solicitado para exibir o processo de cálculo do fatorial
    """
    fatorial = 1
    for c in range(num, 0, -1):
        fatorial *= c
    if show == True:
        print()
        print('Mostrando passo a passo o cálculo de fatorial.')
        print('--' * 30)
        for c in range(num, 0 , -1):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print(f'= {fatorial}')
    print()
    print('--' * 30)
    print(f'O fatorial do número {num} é {fatorial}')


numero = int(input('Digite um número para calcular o fatorial: '))
processo = str(input('Deseja ver o processo do cálculo do fatorial? [S/N] ')).upper().strip()[0]

if processo == 'S':
    fatorial(numero, True)
else:
    fatorial(numero)

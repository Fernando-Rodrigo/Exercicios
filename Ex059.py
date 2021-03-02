"""Crie um programa que leia dois valores e mostre um menu na tela: [1]Somar [2]Multiplicar [3]Maior [4]novos números [5]Sair do programa Seu programa deverá realizar a operação solicitada em cada caso."""

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

opcao = int(input('Qual a opção de operação que deseja realizar: \n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa. '))

while opcao !=5:
    if opcao == 1:
        print('A soma dos valores {} com {} é {}'.format(n1, n2, n1 + n2))
    if opcao == 2:
        print('O resultado da multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    if opcao == 3:
        if n1 > n2:
            print('O maior número digitado é {}'.format(n1))
        else:
            print('O maior número digitado é {}'.format(n2))
    if opcao == 4:
        n1 = float(input('Digite o primeiro valor novo: '))
        n2 = float(input('Digite o segundo valor novo: '))
    opcao = int(input('Qual a opção de operação que deseja realizar: \n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa. '))

print('Fim do programa!!!')

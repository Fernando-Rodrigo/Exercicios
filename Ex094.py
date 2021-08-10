"""Crie um prgrama que leia nome, sexo e idade, guardando os dados da pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadstradas. B)A médida de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média. Deve ter a opção de cadastrar um número variável de pessoas."""

pessoas = []
temp = {}
cont = ''
mediaidade = soma = 0

while True:
    temp['nome'] = str(input('Qual é o nome da pessoa? '))
    while True:
        temp['sexo'] = str(input('Qual é o sexo da pessoa? [M/F] ')).upper().strip()[0]
        if temp["sexo"] in "MF":
            break
        print('Digite somente M ou F!!!')
    temp['idade'] = int(input('Quantos anos tem a pessoa? '))
    soma += temp["idade"]
    pessoas.append(temp.copy())
    temp.clear()
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break

mediaidade = soma / len(pessoas)

print()
print('--'*30)
print(f'Foram cadastradas {len(pessoas)} pessoas na lista.')
print(f'A idade média das pessoas é {mediaidade :.2f} anos.')

print('A lista de mulheres cadastradas é: ', end='')
for p in pessoas:
    if p["sexo"] in 'F':
        print(f'{p["nome"]}', end=' ')
print()

print('A lista de pessoas com idade acima da média é: ')
for i in pessoas:
    if i["idade"] > mediaidade:
        print(f'Nome: {i["nome"]}; sexo: {i["sexo"]}; idade: {i["idade"]}')

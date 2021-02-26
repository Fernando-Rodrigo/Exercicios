"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: -A média de idade do grupo; -Qual é o nome do homem mais velho; -Quantas mulheres têm menos de 20 anos."""

idadetotal = 0
media = 0
maioridade = 0
nomehomem = ''
menoridade = 0

for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}ª pessoa: '.format(i)))

    idadetotal += idade

    if i == 1 and sexo in 'Mm':
        maioridade = idade
        nomehomem = nome
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        nomehomem = nome
    if sexo == 'f':
        if idade < 20:
            menoridade += 1

media = idadetotal / 4

print('A idade média das pessoas é {} anos.'.format(media))
print('O homem mais velho é o {}'.format(nomehomem))
print('Tem {} mulheres com menos de 20 anos.'.format(menoridade))

"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
-se ele ainda vai se alistar no serviço militar;
-se é a hora de se alistar;
-se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

sexo = int(input('Digite 1 para masculino ou 2 para feminino: '))

if sexo == 1:
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        anos = 18 - idade
        anoalis = ano + anos
        print('Ainda vai se alistar no serviço militar e falta {} anos para se alistar.'.format(anos))
        print('Deverá se alistar em {}.'.format(anoalis))
    elif idade == 18:
        print('É hora de se alistar no serviço militar.')
    elif idade > 18:
        anos = idade - 18
        anoalis = date.today().year - anos
        print('Já passou da hora de se alistar no serviço militar e já passou {} anos da idade de se alistar.'.format(anos))
        print('Deveria ter se alistado em {}.'.format(anoalis))
else:
    print('Não precisa se alistar no serviço militar.')

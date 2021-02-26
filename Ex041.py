"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordocom sua idade:
-até 9 anos: mirim;
-até 14 anos: infantil;
-até 19 anos: junior;
-até 20 anos: sênior;
-acima: master."""

from datetime import date

ano = int(input('Digite o ano de nascimento: '))

idade = date.today().year - ano

print('A idade do atleta é {} anos.'.format(idade))

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
elif idade > 25:
    print('Master')

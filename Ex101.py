"""Crie um programa que tenha uma função chamada voto(), que vai receber como parâmetro, o ano de nascimento de uma pessoa(calcular idade), retornando um valor literal(string), indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""

from datetime import datetime

def voto(ano):
    """
    ->Calcula a idade e diz se é não é preciso votar, se é opcional, ou se é obrigatório votar.
    :param ano: ano de nascimento da pessoa
    :return: 'NEGADO' ou 'NEGADO' ou 'OBRIGATÓRIO'
    """
    idade = datetime.now().year - ano
    if idade < 16:
        return 'NEGADO'
    elif idade < 18:
        return 'NEGADO'
    elif idade < 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'


#programaprincipal
ano = int(input('Qual é o ano de nascimento? '))

print()
print('--' * 30)
print(f'A idade é {datetime.now().year - ano} ano(s) e o voto é {voto(ano)}')
print('--' * 30)

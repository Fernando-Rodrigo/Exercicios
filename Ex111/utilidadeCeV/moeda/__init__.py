def resumo(valor, taxa):
    """
    _>Função que recebe o valor monetário e a taxa para cálculo de desconto, aumento, metade e dobro do valor.
    :param valor: Valor monetário
    :param taxa: Valor da taxa para cálculo do desconto e aumento
    """
    print(f'O valor inserido é {moeda(valor)}')
    print(f'Com aumento de {taxa}% fica {aumentar(valor, taxa)}')
    print(f'Com {taxa}% desconto fica {diminuir(valor, taxa)}')
    print(f'O dobro é {dobro(valor)}')
    print(f'A metade é {metade(valor)}')


def aumentar(valor, taxa):
    resultado = valor + (valor * (taxa / 100))
    return moeda(resultado)



def diminuir(valor, taxa):
    resultado = valor - (valor * (taxa / 100))
    return moeda(resultado)


def dobro(valor):
    resultado = valor * 2
    return moeda(resultado)


def metade(valor):
    resultado = valor / 2
    return moeda(resultado)


def moeda(valor, moeda='R$'):
    return f'{moeda}{valor :.2f}'.replace('.', ',')

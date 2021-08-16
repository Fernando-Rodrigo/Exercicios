def aumentar(valor, formatar=False):
    resultado = valor + valor * 0.2
    if formatar == True:
        return moeda(resultado)
    else:
        return resultado


def diminuir(valor, formatar=False):
    resultado = valor - valor * 0.3
    if formatar == True:
        return moeda(resultado)
    else:
        return resultado


def dobro(valor, formatar=False):
    resultado = valor * 2
    if formatar == True:
        return moeda(resultado)
    else:
        return resultado


def metade(valor, formatar=False):
    resultado = valor / 2
    if formatar == True:
        return moeda(resultado)
    else:
        return resultado


def moeda(valor):
    return f'{valor :.2f}'
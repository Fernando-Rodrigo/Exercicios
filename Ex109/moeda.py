def aumentar(valor, taxa, formatar=False):
    resultado = valor + (valor * (taxa / 100))
    if formatar == True:
        return moeda(resultado)
    else:
        return resultado


def diminuir(valor, taxa, formatar=False):
    resultado = valor - (valor * (taxa / 100))
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


def moeda(valor, moeda='R$'):
    return f'{moeda}{valor :.2f}'.replace('.', ',')
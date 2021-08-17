def aumentar(valor, taxa):
    return valor + (valor * (taxa/100))


def diminuir(valor, taxa):
    return valor - (valor * (taxa / 100))


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moeda(valor, moeda='R$'):
    return f'{moeda}{valor :.2f}'.replace('.', ',')

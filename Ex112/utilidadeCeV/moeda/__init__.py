def resumo(valor, taxa):
    return f'\nO valor inserido é {moeda(valor)}\nCom aumento de {taxa}% fica {aumentar(valor, taxa)}\nCom {taxa}% desconto fica {diminuir(valor, taxa)}\nO dobro é {dobro(valor)}\nA metade é {metade(valor)}'


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

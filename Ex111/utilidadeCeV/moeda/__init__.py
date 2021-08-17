def resumo(valor, taxa):
    return f'\nO valor inserido é R${moeda(valor)}\nCom aumento de {moeda(taxa)}% fica R${aumentar(valor, taxa)}\nCom {moeda(taxa)}% desconto fica R${diminuir(valor, taxa)}\nO dobro é R${dobro(valor)}\nA metade é R${metade(valor)}'


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


def moeda(valor):
    return f'{valor :.2f}'
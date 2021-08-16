def resumo(valor):
    return f'\nO valor inserido é R${moeda(valor)}\nCom aumento de 20% fica R${aumentar(valor)}\nCom 30% desconto fica R${diminuir(valor)}\nO dobro é R${dobro(valor)}\nA metade é R${metade(valor)}'


def aumentar(valor):
    resultado = valor + valor * 0.2
    return moeda(resultado)



def diminuir(valor):
    resultado = valor - valor * 0.3
    return moeda(resultado)


def dobro(valor):
    resultado = valor * 2
    return moeda(resultado)


def metade(valor):
    resultado = valor / 2
    return moeda(resultado)


def moeda(valor):
    return f'{valor :.2f}'
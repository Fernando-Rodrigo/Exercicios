import _pyio


def cadastro(nome, idade):
    lista = _pyio.FileIO.readall('../cadastro.csv')
    print(lista)
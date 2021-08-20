from lib.interface import *

def arquivoExiste(arq):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        arquivo = open(arq, 'wt+')
        arquivo.close()
    except:
        cor(4)
        print('Houve erro na criação do arquivo')
    else:
        cor(2)
        print('Arquivo criado')


def lerArquivo(arq):
    try:
        arquivo = open(arq, 'rt')
    except:
        print('Houve erro na leitura')
    else:
        cabecalho('Pessoas cdastradas')
        print(arquivo.readlines())

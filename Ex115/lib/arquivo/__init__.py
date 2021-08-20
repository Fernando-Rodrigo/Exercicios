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
    dado = []
    try:
        arquivo = open(arq, 'rt')
    except:
        print('Houve erro na leitura')
    else:
        cabecalho('Pessoas cdastradas')
        for linha in arquivo:
            cor(10)
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20} {dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        cor(4)
        print('Houve uma falha na abertura do arquivo')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            cor(4)
            print('Houve um erro para cadastrar')
        else:
            cor(5)
            print(f'Registro de {nome} adicionado.')
            arquivo.close()

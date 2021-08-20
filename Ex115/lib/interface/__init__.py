from ctypes import windll

def cor(numcor):
    std_out_handle = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.SetConsoleTextAttribute(std_out_handle, numcor)

def leiaInt(msg):
    while True:
        try:
            cor(1)
            n = int(input(msg))
            return n
            break
        except(ValueError, TypeError):
            cor(4)
            print('Digite somente valores inteiros')


def linha(tam=30):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabecalho('Menu de opções')
    for i in range(0, 3):
        print(f'{i + 1} - {lista[i]}')
    print(linha())
    opcao = leiaInt('Qual a opção que deseja? ')
    return opcao

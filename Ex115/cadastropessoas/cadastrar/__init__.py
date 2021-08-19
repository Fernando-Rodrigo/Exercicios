from ctypes import windll

std_out_handle = windll.kernel32.GetStdHandle(-11)

lista = {}

with open('./Ex115/cadastropessoas/cadastro') as f:
    read_data = f.read()


def cadastro():
    windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    while True:
        try:
            nome = str(input('Nome: '))
            break
        except (ValueError, TypeError):
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
            print('Digite somente nome')
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except (ValueError, TypeError):
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
            print('Digite somente idade')
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    lista = {nome:idade}
    idadestr = str(lista)
    f = open('./Ex115/cadastropessoas/cadastro', 'a')
    f.write(idadestr)
    f.write('\n')
    f.close()

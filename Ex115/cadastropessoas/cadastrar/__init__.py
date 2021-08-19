lista = {}

with open('./Ex115/cadastropessoas/cadastro') as f:
    read_data = f.read()


def cadastro():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    idadestr = str(idade)
    f = open('./Ex115/cadastropessoas/cadastro', 'a')
    f.write(nome)
    f.write('\n')
    f.write(idadestr)
    f.write('\n')
    f.close()

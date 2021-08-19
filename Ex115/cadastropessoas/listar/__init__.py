with open('./Ex115/cadastropessoas/cadastro') as f:
    read_data = f.read()

def listar():
    f = open('./Ex115/cadastropessoas/cadastro')
    print()
    print('--' * 15)
    print('Pessoas cadastradas')
    print('--' * 15)
    print('Nome', f'Idade')
    for k,v in enumerate(f):
        print(f'{k} {v}')
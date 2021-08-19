with open('./Ex115/cadastropessoas/cadastro', 'r') as f:
    read_data = f.read()

def listar():
    dados = []
    f = open('./Ex115/cadastropessoas/cadastro', 'r')
    for line in f:
        dados.append(line)
    print()
    print('--' * 15)
    print('Pessoas cadastradas')
    print('--' * 15)
    print('Nome', f'Idade')
    c = 0
    while c < len(dados):
        print(f'{dados[c]}', end='')
        print(f'{dados[c + 1]}')
        c += 2
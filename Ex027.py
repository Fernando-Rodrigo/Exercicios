nome = str(input('Digite o nome completo de uma pessoa ')).strip()

ns = nome.split()
# t = len(ns)

print('O primeiro nome da pessoa é: {}'.format(ns[0]))
print('O ultimo nome é: {}'.format(ns[len(ns)-1]))

import random

n1 = input('Primeiro aluno ')
n2 = input('Segundo aluno ')
n3 = input('Terceiro aluno ')
n4 = input('Quarto aluno ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)
# Não é necessário atribuir o resultado a uma variável.
# Basta usar a mesma variável da lista para mostrar o resultado.

print('A ordem de apresentação será ')
print(lista)

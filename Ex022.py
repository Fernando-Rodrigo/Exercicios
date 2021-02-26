nome = str(input('Digite um nome completo de uma pessoa ')).strip()

print('O nome completo e maiusculas é {}'.format(nome.upper()))
print('O nome completo em minusculas é {}'.format(nome.lower()))
strs = nome.split()
print('O nome sem os espaços tem {} caracteres'.format(len(''.join(strs))))
print('O primeiro nome tem {} caracteres.'.format(len(strs[0])))

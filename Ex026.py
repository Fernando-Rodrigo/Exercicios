frase = str(input('Digite uma frase ')).strip()

fl = frase.lower()

print('Na frase digitada a letra "a" aparece {} vezes.'.format(fl.count('a')))
print('A posição do primeiro "a" é: {}'.format(fl.find('a')+1))
print('A posição do ultimo "a" é: {}'.format(fl.rfind('a')+1))

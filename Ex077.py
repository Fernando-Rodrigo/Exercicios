"""Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('Ola', 'Boi', 'Python')

for i in palavras:
    print(f'\nAs vogais da palavra {i} são ', end='')
    for letras in i:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')

"""Faça um programa que tenha a função escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com com tamanho adaptável. Ex: escreva('olá, mundo!') saída: ----------- Olá, mundo! -----------"""

def escreva(frase):
    print('--' * len(frase))
    print(' ' * ((len(frase)//2) - 1), frase)
    print('--' * len(frase))


escreva('casarão')
escreva('casa')
escreva('escola')
escreva('Curso em vídeo')
escreva('Super casa automática')

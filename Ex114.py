"""Crie um código em Python que teste se o site Pudim está acessível pelo computador usado."""

from http.client import HTTPConnection
from ctypes import windll

def cor(texto, cornum):
    std_out_handle = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.SetConsoleTextAttribute(std_out_handle, cornum)
    print(f'{texto}')
    # cor padrão é 7, white
    windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)


try:
    HTTPConnection('pudim.com.br/')
    texto='O site está no ar!!!'
    cor(texto, 2)
except:
    texto='O site está fora do ar!!!'
    cor(texto, 4)

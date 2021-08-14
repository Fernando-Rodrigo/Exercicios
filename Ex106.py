"""Faça um mini-programa que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: use cores."""


def ajuda(comando):
    help(comando)


while True:
    cmd = str(input('\33[30;46mQual é o comando que deseja ver o manual? (FIM para encerrar) '))
    if cmd in 'FIMFimfim':
        break
    ajuda(cmd)

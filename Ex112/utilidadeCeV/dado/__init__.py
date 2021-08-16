def leiaDinheiro(num):
    from sys import stdout
    from ctypes import windll

    validade = False
    valor = 0
    color = [4]
    texto = 'Você deve digitar somente valores monetários'
    std_out_handle = windll.kernel32.GetStdHandle(-11)
    while True:
        valor = str(input(num))
        if valor.isdecimal():
            valor = float(valor)
            validade = True
        else:
            for i in range(0, len(color)):
                windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
                stdout.write(texto)
                print('')
            # cor padrão é 7, white
            windll.kernel32.SetConsoleTextAttribute(std_out_handle, 4)
        windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
        if validade:
            break
    return valor

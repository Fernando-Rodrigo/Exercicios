tempc1 = float(input('Digite uma temperatura em graus Celcius para converter para Farenheit: '))

tempf1 = 32 + (tempc1 * 9/5)

print('A temperatura de {:.2f}°C é em {:.2f}ºF'.format(tempc1, tempf1))

tempf2 = float(input('Digite uma temperatura em Farenheit para converter para Celsius: '))

tempc2 = (tempf2 - 32) * 5/9

print('A temperatura {:.2f}°F é em {:.2f}°C'.format(tempf2, tempc2))

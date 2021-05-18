"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deve analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

expressao = []

count1 = count2 = 0

expressaostr = str(input('Digite a expressão matemática: ')).split()

# expressao.append(input('Digite a expressão matemática: '))

for i in range (0, len(expressaostr)):
    if expressaostr[i] == '(':
        count1 += 1
    elif expressaostr[i] == ')':
        count2 += 1

print(f'{count1}')

"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deve analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

expressao = []

expressaostr = str(input('Digite a expressão matemática: '))

# expressao.append(input('Digite a expressão matemática: '))

for i in expressaostr:
    if i == '(':
        expressao.append('(')
    elif i == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break

if len(expressao) == 0:
    print('A expressão digitada é válida!!!')
else:
    print('A expressão digitada é inválida!!!')

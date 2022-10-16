numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

print('Operações disponíveis:\n\t+ para Adição\n\t- para Subtração\n\t* para Multiplicação\n\t/ para Divisão')

operacao = input('Digite a operação: ')

equacao = f'{numero_1} {operacao} {numero_2}'

resultado = eval(equacao)

print(f'{"*" * 20}\nResultado: {resultado}\n{"*" * 20}')

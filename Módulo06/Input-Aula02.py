# nome = input('Qual é o seu nome: ')
#
# print(nome)

# Entrada
numero = input('Digite um número: ')
expoente = input('Digite um expoente: ')

# Processamento
resultado = int(numero) ** int(expoente)

# Saída
print(f' O resultado de {numero} elevado à {expoente} é {resultado}.')

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
altura = input('Qual a sua altura? ')

print('Os dados inseridos foram: ')
print(
    f'\tNome: {nome}\n'
    f'\tIdade: {idade} anos\n'
    f'\tAltura: {float(altura):.2f}'
)

# SETs = Conjuntos matemáticos
# - Desordenados
# - Itens não intercambiáveis
# - Não são indexados
# - Não possuem elementos duplicados
# - Possiem métodos para manipulação de conjuntos

# Criando Sets

set_1 = {1, 2, 3}

print(set_1)
print(type(set_1))

set_2 = set()  # Set vazio

lista = [1, 2, 3]  # Podemos incluir uma lista dentro de um set
set_2 = set(lista)

print(set_2)

# Manipulando SETs

carteira = {'PETR4', 'CASH3', 'MGLU3', 'BBAS3', 'WEGE3'}  # A ordem dos elementos não importa

print(f'Carteira inicial: {carteira}')

# ADD, adicionar elementos

carteira.add('PETR4')  # Set não aceita elementos repetidos, será mantido somente 1 dos valores
carteira.add('ITSA4')

print(f'Carteira após add: {carteira}')

# Atualizando elementos com UPDATE

carteira.update({'PETR4', 'ABEV3', 'RAIZ4'})  # Adiciona somente os itens não existentes

print(f'Carteira após update: {carteira}')

# Remover elementos com DISCARD

carteira.discard('PETR4')

print(f'Carteira após discard: {carteira}')

# Removendo elementos com REMOVE, caso o elemento não estiver no set retornará um erro

carteira.remove('ABEV3')

# carteira.remove('BBSE3')  # KeyError, elemento não existente no set

print(f'Carteira após remove: {carteira}')

# Retirarndo elemento com POP, remove ultimo elemento (Cuidado, pois os elementos estão dispostos de forma aleatória)
# Retorma o item que foi removido

item = carteira.pop()

print(f'O item removido foi: {item}')
print(f'Carteira após o pop: {carteira}')

# Limpando TODOS os elementos com CLEAR

carteira.clear()

print(f'Carteira após o clear: {carteira}')

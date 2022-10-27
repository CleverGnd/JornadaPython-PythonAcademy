# Tuplas
# - Ordenados
# - Permite valores duplicados
# - Indexados
# - Permite dados Heterogêneos
# - Elementos não-intercambiáveis

# Criação de Tuplas

tupla = (1, 2, 3)

print(type(tupla))
print(tupla)

lista = [5, 6, 7]
tupla_2 = tuple(lista)  # Criar tupla vazia e a partir de uma lista

print(tupla_2)

tupla = ()  # Tupla vazia

print(type(tupla))

tupla = (1)  # Tupla somente com 1 valor, no caso int

print(type(tupla))  # Como possui somente 1 elemento, consta como int

tupla = (1,)  # Ao adicionar a virgula, o python reconhece o type como tupla

print(type(tupla))

# Indexação

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tupla)
print(f'O quinto elemento da Tupla é: {tupla[4]}')

# Indexação Negativa

print(f'0 último elemento da Tupla é: {tupla[-1]}')

# Slicing, fatiamento

tupla_slicing = tupla[4:]  # Do elemento 5 até o final
print(tupla_slicing)

# Tentativa de alteração de valores, não permitido

# tupla[0] = 1  # TypeError: 'tuple' object does not support item assignment

# Deleção com del, em tupla não é possível deletar somente 1 elemento

# del tupla[0]  # TypeError: 'tuple' object doesn't support item deletion

# del tupla  # Deleta toda a tupla
# print(tupla)  # NameError: name 'tupla' is not defined. (Foi totalmente excluída

# Métodos

# Count, contar elementos

print(f'A quantidade de elementos iguais à 1 é: {tupla.count(1)}')  # Contar quantas vezes o elemento () aparece na tupla

# Index, retorna o índice do elemento ()
print(f'0 elemento 10 está na posição: {tupla.index(10)}')

# Iteração, passar por todos os elementos

for elemento in tupla:
    print(f'Elemento = {elemento}')

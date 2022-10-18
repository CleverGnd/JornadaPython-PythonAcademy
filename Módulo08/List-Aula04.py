#          0    1    2    3    4    5
letras = ['a', 'b', 'c', 'd', 'e', 'f']
#         -6   -5   -4   -3   -2   -1

# Dividir uma lista
print(letras[0:3:1])  # Do início até o elemento 2
print(letras[3:6:1])  # Do elemento 3 até o elemento 5
print(letras[::-1])  # Inverter a ordem da lista

print(letras[-6:-3:1])  # Indexação negativa
print(letras[-3::1])

# Pular elementos
print(letras[::2])
print(letras[1::2])  # Pular primeiro elemento

# Concatenar lista
print(letras[::2] + letras[1::2])
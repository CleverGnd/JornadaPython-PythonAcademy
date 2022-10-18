lista = []

print(lista)
print(type(lista))

lista = list([])

print(lista)
print(type(lista))

lista = [0, 'str', 5.5, []]

print(lista)

for elemento in lista:
    print(f'O elemento atual é {elemento}')

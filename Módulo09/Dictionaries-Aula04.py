# Criar um dicionário

fila = {
    '0': 'João',
    '1': 'Joana',
    '2': 'Clara',
    '3': 'Ana',
    '4': 'Julio'
}

print(f'Fila inicial: {fila}')

# Remover elemento 'del'

del fila['0']  # Deleta a chave e valor ao mesmo tempo

print(fila)

# Remover elemento 'pop', deleta a chave e pode retornar o valor que estava na chave

valor_removido = fila.pop('1')

print(f'Valor removido com pop: {valor_removido}')
print(fila)

# Popitem, deleta sempre o último elemento

valor_removido2 = fila.popitem()
print(f'Valor removido com popitem: {valor_removido2}')
print(fila)

# clear, limpa TODAS as chaves e elementos

fila.clear()
print(fila)

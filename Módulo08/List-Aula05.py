sacola = ['Arroz', 'Feijão', 'Carne', 'Farinha']

print(f'A Lista inicial é: {sacola}')

# Método: APPEND(objeto) - Adiciona um item ao final da lista

sacola.append('Macarão')
print(f'A Lista após o append é: {sacola}')

# Método: EXTEND(estruturas) - Adiciona todos os itens de outra estrutura ao fim da lista

sacola.extend(['Maionese', 'Ketchup'])
print(f'A Lista após o extend é: {sacola}')

# Método: INSERT(índice, objeto) -  Insere um item em uma posição desejada

sacola.insert(0, 'Milho')
print(f'A Lista após o insert é: {sacola}')

# Método: REMOVE(objeto) - Remove o primeiro elemento igual ao valor passado

sacola.remove('Macarão')
print(f'A Lista após o remove é: {sacola}')

# Método: POP(índice) - Remove o item da posição desejada da lista e o retorna
# Caso o índice não seja especificado, retorna o último elemento

sacola.pop()
print(f'A Lista após o pop sem indicar índice é: {sacola}')

elemento = sacola.pop(3)
print(f'A Lista após o pop com índice é: {sacola}')
print(f'O elemento removido foi: {elemento}')

# Método: CLEAR() - Remove todos os elementos da lista

sacola.clear()
print(f'A Lista após o clear é: {sacola}')


sacola = ['Milho', 'Arroz', 'Feijão', 'Carne', 'Farinha', 'Macarão', 'Maionese', 'Ketchup']

# Método: INDEX(valor[, começo, fim]) - Retorna o índice do primeiro elemento do valor especificado
# Podemos ainda passar outros dois parâmetros que dizem onde pesquisar na lista (começo e fim)

print(sacola.index('Farinha'))
print(f'O elemento Milho esta no índice {sacola.index("Milho")}')

# Informar um elemento inexistente:
# print(sacola.index('Alface'))
# ValueError: 'Alface' is not in list

# Método: COUNT(valor) - Conta o número de ocorrências do valor especificado na lista

print(sacola.count('Arroz'))

# Método: SORT([chave, reverso]) - Ordena os itens da lista
# Parâmetros adicionais podem ser utilizados para customizar a ordenação

sacola.sort()
print(f'A Lista após o sort é: {sacola}')

sacola.sort(reverse=True)
print(f'A Lista após o sort reverso é: {sacola}')

# Método: REVERSE() - Reverte os elementos da lista

sacola = ['Milho', 'Arroz', 'Feijão', 'Carne', 'Farinha', 'Macarão', 'Maionese', 'Ketchup']

print(f'A Lista original é: {sacola}')

sacola.reverse()

print(f'A Lista após reverse é: {sacola}')

# Método: COPY() - Retorna uma lista com uma cópia dos elementos da lista origem

copia_sacola = sacola.copy()
print(f'A cópia da lista com copy é: {copia_sacola}')

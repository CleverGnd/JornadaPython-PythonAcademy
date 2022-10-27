# Operações matemáticas com SETs

homens = {'João', 'Joaquim', 'Alberto', 'Antônio', 'Leonardo', 'Victor', 'Kléber', 'Marcelo', 'Alfredo'}
alta_renda = {'Ana', 'Joaquim', 'Joana', 'Antônio', 'Kléber', 'Marcelo', 'Alfredo', 'Carla', 'Adriana'}

print(f'Conjunto de Homens: \t{homens}')
print(f'Conjunto de Alta Renda: : {alta_renda}\n {"- "* 100}\n')

# Intersecao: Itens que estão em ambos os conjuntos

homens_alta_renda = homens.intersection(alta_renda)

print(f'Usuários Homens com Alta Renda: {homens_alta_renda}')

# União: Itens de ambos os conjuntos (Juntar os 2 conjuntos)

homens_e_alta_renda = homens_alta_renda.union(homens)

print(f'Homens e Usuários con Alta Renda: {homens_e_alta_renda}')

# Diferença: Itens que estão apenas em um dos conjuntos

homens_nao_alta_renda = homens.difference(alta_renda)
alta_renda_nao_homens = alta_renda.difference(homens)

print(f'Usuários Homens que não estão em Alta Renda: {homens_nao_alta_renda}')
print(f'Usuários Alta Renda que não são Homens: {alta_renda_nao_homens}')

# Diferença Simétrica: Itens em um conjunto ou em outro mas não em ambos (Itens não repetidos entre 2 conjuntos)

homens_nao_alta_renda_e_mulheres = homens.symmetric_difference(alta_renda)

print(f'Usuários Homens não Alta Renda e Usuárias Mulheres Alta Renda: {homens_nao_alta_renda_e_mulheres}')

# Usando os comandos acima, com _update irá alterar o conjunto original, não retornando nada

# Métodos de Conjuntos

# Se conjuntos são separados, não tiverem nenhum elemento em comum
print(f'Os conjuntos de Homens e Alta Renda são disjuntos? {homens.isdisjoint(alta_renda)}')

# Se um conjunto está contido em outro
print(f'0 conjunto de Homens é um subconjunto de Alta Renda? {homens.issubset(alta_renda)}')

# Para dois conjuntos A e B, se A é um subconjunto de B, então B é o superconjunto de A. A pode ser igual a B
print(f'O conjunto de Homens é um superconjunto de Alta Renda? {homens.issuperset(alta_renda)}')

# Notações simplificadas
# Interseção
print(homens & alta_renda)

# União
print(homens | alta_renda)

# Diferença
print(homens - alta_renda)

# f string python
titulo = 'Monitor Gamer'
polegadas = 27

print(f'Nome do Produto: {titulo} e Tamanhp: {polegadas}".')

# Multilinhas
preco = 1299.99
print(
    f'Produto: {titulo.upper()}\n'
    f'Tamanho: {polegadas} polegadas\n'
    f'Preço: R$ {preco}'
)

# Formatadores especiais
print(
    f'Produto: {titulo.upper():*^30}\n'  # *(caracteres) ^(alinhamento centralizado) 30(espaços contado com a string)
    f'Tamanho: {polegadas} polegadas\n'
    f'Preço: R$ {preco}'
)

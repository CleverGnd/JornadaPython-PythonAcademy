# Criar um dicionário

familia = {
    'pai': 'José da Silva',
    'mae': 'Ana Almeida',
    'filho': 'Cléber da Silva Almeira',
    'filha': 'Joana da Silva Almeida'
}

print(f'Família : {familia}')

# Copy, copiar um dicionário

copia_familia = familia.copy()

print(f'Cópia do dicionário família: {copia_familia}')

# Items, retorna os pares chave: valor em formato de lista

itens = familia.items()

print(f'Itens: {itens}')

for item in itens:  # Percorrer itens
    print(f'\tChave = {item[0]} e Valor = {item[1]}')

# Keys, retorna todas as chaves em formato de lista

chaves = familia.keys()

print(f'Chaves: {chaves}')

for chave in chaves:
    print(f'\tChave: {chave}')

# Values, retorna todos os valores em formato de lista

valores = familia.values()

print(f'Valores: {valores}')

for valor in valores:
    print(f'\tValor: {valor}')

# SetDefault, Insere a chave com o valor passado SE a chave não estiver no dicionário
# Retorna o valor da chave SE a chave já estiver presente no dicionário

familia.setdefault('sobrinho', 'Carlos Silva')

print(f'Família : {familia}')

# Com chave existente

mae = familia.setdefault('mae', 'Dona Florinda')  # Chave existente, não irá substituir o valor original

print(f'Família : {familia}')
print(f'Retorno do setdefault : {mae}')

# FromKeys, cria um dicionário a partir de uma lista de chaves e um valor

chaves = ['mae', 'pai', 'filho', 'filha']
valor = 0

jogo = dict.fromkeys(chaves, valor)

print(jogo)

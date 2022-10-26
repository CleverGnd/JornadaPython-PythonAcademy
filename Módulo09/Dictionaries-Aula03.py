# Criar um dicionário

computador = {
    'cpu': 'Core i7',
    'ram': 'DDR 16 Gb',
    'ssd': 'Samsung Evo 840 256 Gb',
    'gpu': 'RTX 2080 Ti'
}

print(f'Computador v1: {computador}')

# Atualizar valores de um dicionário

computador['ram'] = 'DDR4 32 Gb'

print(f'Computador v2: {computador}')

# Incluir uma nova key e valor

computador['fonte'] = 'Fonte 600 W Corsair'

print(f'Computador v3: {computador}')

# Atualizar com método
# Podemos alterar mais de um elemento ao mesmo tempo

computador.update({'fonte': 'Fonte 850 W Corsair', 'ssd': 'Samsung Evo 840 1 Tb'})

print(f'Computador v4: {computador}')

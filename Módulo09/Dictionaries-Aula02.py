# Criar um dicionário

cadastro = {
    'id' : 1,
    'nome' : 'João Carlos',
    'filhos' : ['Joana', 'Sarah'],  # Uma lista dentro de um dicionário
    'compras' : [  # Um dicionário dentro de outro dicionário
        {
            'id' : 4758,
            'produto' : 'Notebook Gamer',
            'preço' : 2597.99
        }
    ]
}

# Acessar dados em um dicionário


print(cadastro)
print(cadastro['nome'])
print(cadastro['compras'])
print(cadastro['compras'][0])

# Acessando dados

print(f'O usuário {cadastro["nome"]} realizou a seguinte compra: {cadastro["compras"][0]["produto"]}')

# Simplificando o acesso dos dados

notebook_gamer = cadastro["compras"][0]

print(f'O usuário {cadastro["nome"]} realizou a seguinte compra: {notebook_gamer["produto"]}')

# Método GET

filhos = cadastro.get('filhos')  # Possui um segundo parametro

print(filhos)

# print(cadastro['altura'])  # Erro KeyError, key inexistente

altura = cadastro.get('altura', None) # Ao utilizar uma key invalida, retorna None (tratamento de erro)

print(altura)

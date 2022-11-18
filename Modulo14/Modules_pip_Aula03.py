# Biblioteca padrão do Python
# Módulos pré-instalados no python https://docs.python.org/3/py-modindex.html
import base64
import json
import os
import random
import string

# Utilizando módulo base64

with open('./logo.png', 'rb') as arquivo:
    arquivo_b64 = base64.b64encode(arquivo.read())

    print(arquivo_b64)  # Retorna a imagem codigicada em base 64
    # Para decodificar para png novamente -> https://base64.guru/converter/decode/image/png


# Utilizando módulo json

cadastros = [  # Criar dicionário
    {
        'Nome': 'João',
        'Idade': 31,
        'Profissões': ['Estagiário', 'Dev Python', 'Engenheiro de Software']
    }, {
        'Nome': 'Clara',
        'Idade': 35,
        'Profissões': ['Estagiária de Design', 'Desenvolvedora Frontend']
    }
]

# Cria json com dados do dicionário, e corrige a formatação dos acentos. Cria indentação
print(json.dumps(cadastros, ensure_ascii=False, indent=True))


# Utilizando módulo os

# os.mkdir('./Nova Pasta')  # Cria novas pastas

# Listando diretórios
# for diretorio in os.listdir('./'):
#     print(diretorio)

# Verificar se pasta existe, caso negativo criar a pasta
# if os.path.exists('./Nova Pasta[2]'):
#     print('A "Nova Pasta[2]" já existe!')
# else:
#     os.mkdir('./Nova Pasta[2]')
#
# os.rmdir('./Nova Pasta[2]')  # Remover a pasta
#
# print(os.getcwd()) # Posta o diretório atual

# os.rename('./logo.png', '/logo_curso.png')  # Renomear aquivo existente

# print(os.path.getsize('./logo.png'))  # Tamanho do arquivo em bytes

print(string.ascii_letters)  # Retorna todas as letras maiúsculas e minúsculas

print(random.choice('abcd'))  # Escolhe um caracter aleatório

print(random.choice(string.ascii_letters))

tamanho_senha = int(input('Tamanho da Senha: '))
senha = []

for i in range(0, tamanho_senha):  # Criar uma senha aleatória de X carácteres
    senha.append(random.choice(string.ascii_letters))

print(''.join(senha))  # Juntar elementos da lista

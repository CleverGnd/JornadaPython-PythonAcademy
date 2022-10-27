# Funções em Python

# Função Bem-vindo!

# Exemplo convencional, para cada alteração seri necessário copiar e alterar o código abaixo:
nome = 'Antônio'
idade = 50
emprego = 'Desenvolvedor Frontend'

print(f'Olá! Meu nome é {nome}, tenho {idade} anos e trabalho como {emprego}')

# Criando uma função, para tarefas repetidas

def diz_ola(nome, idade, emprego):
    print(f'Olá! Meu nome é {nome}, tenho {idade} anos e trabalho como {emprego}')

# Aplicando a função, facilita a repetição

diz_ola('Carlos', 50, 'Desenvolvedor Frontend')
diz_ola('Joana', 35, 'Desenvolvedora Backend')
diz_ola('Antônio', 22, 'Estagiário de Desenvolvimento')

# Função de somar dois números

def soma(numero_1, numero_2):
    return numero_1 + numero_2

print(soma(10, 20))
print(soma(1, 2))

# Funções com retornos múltiplos

def calcula_media_mediana(lista_notas):
    # sum soma todos os valores de uma lista / len retorna a quantidade de valores em uma lista
    media = sum(lista_notas) / len(lista_notas)

    # Verificar se número de elementos é par ou impar, para realizar o calculo da mediana
    if len(lista_notas) % 2 == 0:
        # Número par de elementos:
        indice_ponto_central_menor = int(len(lista_notas) / 2 - 1)
        indice_ponto_central_maior = int(len(lista_notas) / 2)
        ponto_central_menor = lista_notas[indice_ponto_central_menor]
        ponto_central_maior = lista_notas[indice_ponto_central_maior]

        mediana = (ponto_central_menor + ponto_central_maior) / 2

    else:
        # Número impar de elementos:
        # Ordenar elementos de uma lista
        notas_ordenadas = sorted(lista_notas)
        indice_mediana = int(len(lista_notas) / 2)  # Int pega somente o valor inteiro da divisão
        mediana = notas_ordenadas[indice_mediana]

    return media, mediana  # Retornando múltiplos valores

# Aplicação:


resultado_media, resultado_mediana = calcula_media_mediana([5, 6, 4, 5])  # Pegar os dois valores da função

print(resultado_media)
print(resultado_mediana)



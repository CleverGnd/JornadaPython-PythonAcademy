# Tratamento de erros com Try e Except

# Cadastro com: Nome, Idade, Cargo
cadastro_csv = [
    'João,28,Analista de Sistemas',
    'Maria,31,Desenvolvedora Frontend',
    'Jonas,37,Gerente de Projetos',
    'Luigi,21i,Estagiário',  # Erro proposital para correção (Erro: invalid literal for int() with base 10: '21i')
    'Alberto,47'  # Erro proposital para correção (IndexError: list index out of range)

]


def processa_dados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(',')

        if len(dados) != 3:
            raise ValueError('Formato incorreto dos dados!')  # Definir tipo de Erro e customizar mensagem do erro

        nome = dados[0]

        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError('Erro no formato de dado "Idade"!')  # Customizar mensagem de erro, facilitar usuário

        cargo = dados[2]

        print(f'{nome} tem {idade} anos e exerce o cargo de {cargo}')


# Aplicação da função

try:
    processa_dados(cadastro_csv)

except ValueError as excecao:  # Limpar traceback e apresentar erro identificado para o usuário
    print(f'O programa encontrou um erro. Erro: {excecao}')

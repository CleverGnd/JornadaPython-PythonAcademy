'''
1)	Ler arquive de entrada CSV
2)	Processamento (Retirada do campo ID e junção do campo NOME e SOBRENOME)
5) Gravação dc arquivo de CSV de saida
'''

resultados = []

with open('./Cadastro.csv', 'r') as arquivo_entrada:
    # ./ Mesmo caminho do arquivo atual, o with não necessida o fechamento do arquivo
    linhas = arquivo_entrada.readlines()[1:]  # Retorna todas as linhas de texto do arquivo, [1:] remove a primeira linha

    for linha in linhas:
        dados = linha.split(',')  # Separa os dados das linhas quando encontrar ","
        email = dados[3].replace("\n", "")  # Altera os valor \n para vazio, tem no final de cada e-mail
        resultados.append(f'{dados[1]} {dados[2]}, {email}\n')  # Recria a linha de forma visual

with open('./cadastro_saida.csv', 'w') as arquivo_saida:  # Cria novo arquivo
    for resultado in resultados:  # Para cada itens do resultados, escreve no novo arquivo
        arquivo_saida.write(resultado)






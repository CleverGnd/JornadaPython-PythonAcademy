idade = 35
# texto = 'Parabéns João pelos seus ' + idade + ' anos de idade!'
# print(texto)
# Erro, não conseguimos concatenar um int dentro de uma string

texto = 'Parabéns João pelos seus ' + str(idade) + ' anos de idade!'

print(texto)

pontuacao_str = '10'
pontuacao_int = int(pontuacao_str)

print(pontuacao_int)
print(f'Tipo: {type(pontuacao_int)}')

pontuacao_str = '5.5' # NÃO pode usar virgula ","
pontuacao_float = float(pontuacao_str)

print(pontuacao_float)
print(f'Tipo: {type(pontuacao_float)}')

# print(int('5.5')) # Erro não consegue converter float para int

print(float('1')) # Conseguimos converter um int para float



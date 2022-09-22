nome = 'Guido'
sobrenome = 'van Rossum'

# Concatenação de strings
nome_completo = nome + ' ' + sobrenome

print(nome_completo)
print(nome + ' ' + sobrenome)

# .lower = Todas minúsculas
print(nome_completo.lower())


nome = '    Guido    '
sobrenome = 'van Rossum    '
nome_completo = nome + ' ' + sobrenome
print(nome_completo.lower())
# Remove espaços em branco antes e após as strings
nome_completo = nome.strip() + ' ' + sobrenome.strip()
print(nome_completo.lower())

# Caracteres especiais
print(nome_completo + ' é o criador da Linguagem de Programação Python')
# /n - quebra de linha
# /t = tab (criar um espaçamento)
print('\t' + nome_completo + ' é o criador da \nLinguagem de Programação Python')

# Utilizar " e ' na string = \'
print('\t' + nome_completo + ' é \'o criador da \nLinguagem de Programação Python\'')

# string
mes = str('Janeiro')




# Format
nome = 'João'
sobrenome = 'Oliveira'
idade = 30

print('Meu nome é {} {} e tenho {} anos.'.format(nome, sobrenome, idade))
# Definir quais variáveis serão substituídas
print('Meu nome é {nome} {sobrenome} e tenho {idade} anos.'.format(nome=nome, sobrenome=sobrenome, idade=idade))

# Tabalhando com números
valor = 547.58

print(f'O valor é R$ {valor}'. format(valor=valor))

# .1f = somente 1 casa decimal e arredondando o valor
print(f'O valor é R$ {valor:.1f}'. format(valor=valor))
print(valor)  # Não altera o valor da string!

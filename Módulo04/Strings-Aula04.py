print(' Strip '.strip())
print('maiúsculo'.upper())
print('MINUSCULE'. lower())
print('T, ext, c,o,ma,ria,s v,ir,g,ula s'.replace(',', '')) # Troca um carácter por outro
print('Text test para funçao count'.count('e')) # Conta o número de ocorrências
print('Texto Centralizado'.center(50, '*')) # Centraliza em 50, preenchendo com *
print('Avião?'.index('ã')) # Mostra a primeira posição do carácter ã
print('Alfanumérico'.isnumeric()) # Verifica se os carácteres são numéricos ou não
print('10'.isnumeric()) # Verifica se os carácteres são numéricos ou não
print('Teste de quebra de string com split'.split(' ')) # Quebra em determinado carácter
print('NAME; CIDADE; IDADE; PAIS'.split(';')) # Aplicado em arquivos csv, quebra em substrings
print('este é um titulo'.title()) # A primeira letra de cada palavra fica em maiúsculo
print('este é um título'.capitalize()) # Apenas o primeiro carácter fica em maiúsculo
print('585'.zfill(5)) # Completa com zero a esquerda strings

# Encadeamento de Funções (várias funções aplicadas junto)
print('    Te;x;;to       '.strip().replace(';', '').center(25, '*').upper())

# Tamanho de Strings
string_extensa = 'Essa é uma string extensa. Como faremos ' \
                 'para saber seu tamanho?'
print(len(string_extensa))

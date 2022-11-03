# Tratamento de erros com Try e Except

""" Bloco de verificação de Erros
try:
    # Código a ser testado
except:
    # Execute esse código caso um erro ocorra
else:
    # Execute esse código caso nenhum erro ocorra
finally:
    # Sempre execute esse código
"""

def divide_dois_numeros(dividendo, divisor):  # Função para dividir
    return dividendo/divisor


try:
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))

    resultado = divide_dois_numeros(numero_1, numero_2)

# except ZeroDivisionError:
#     print('Divisão por zero não suportada!')
#
# except TypeError:
#     print('Erro de tipo:')

# Podemos juntar erros na mesma except
except (ZeroDivisionError, TypeError) as excecao:
    print(f'Divisão por zero ou Erro de tipo! Erro: {excecao}')

except Exception:
    print('Um erro ocorreu!')  # Para qualquer erro apresentado

else:
    print(resultado)

finally:
    print('Finalizando programa... Muito obrigado!')





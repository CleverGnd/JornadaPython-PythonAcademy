# Principais erros e exceções

def divide_dois_numeros(dividendo, divisor):  # Função para dividir
    return dividendo/divisor


numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

resultado = divide_dois_numeros(numero_1, numero_2)

print(resultado)

# Erro - ZeroDivisionError: division by zero (Tentar dividir por zero) quando numero_2 = 0
# NameError: name 'divisoir' is not defined. Did you mean: 'divisor'? (Nome de uma variável não definida)
# TypeError: unsupported operand type(s) for /: 'str' and 'int' (Operação não suportada, tentando dividir str
# IndentationError: expected an indented block after function definition on line 3 (Erro de indentação)




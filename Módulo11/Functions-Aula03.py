# Funções em Python - Argumentos posicionais

def funcao_com_args(arg1, arg2, *args):  # Função de múltiplos argumentos
    print(f' Arg1: {arg1}')
    print(f' Arg1: {arg2}')
    print(f'*Args: {args}')


funcao_com_args(1, 2, 3, 4, 5, 6, 7)

# Melhorando a função soma

def soma(*numeros):  # Somar vários números
    resultado = 0

    for numero in numeros:
        resultado += numero

    return resultado


resultado_soma = soma(1, 2, 5)  # Indiferente a quantidade de valores informados, a função continua a funcionar

print(resultado_soma)

# Definir um limite para a função soma

def soma(maximo, *numeros):  # Somar vários números
    resultado = 0
    numeros_somados = []

    for numero in numeros:

        if (resultado + numero) > maximo:
            break

        resultado += numero
        numeros_somados.append(numero)

    return resultado, numeros_somados


resultado_soma, numeros_somados = soma(100, 1, 2, 5, 25, 35, 45, 20, 60)
# Irá realizar a soma dos números até chegar em 100

print(resultado_soma)
print(numeros_somados)
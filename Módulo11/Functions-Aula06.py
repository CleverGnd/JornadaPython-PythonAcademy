# Funções em Python - Dicas de Tipos (Type hints)

def aplica_desconto(produtos: dict, desconto: float) -> dict[str: str]:  # É esperado uma entrada de type dict e float
    # E -> dict, é o type esperado do return. Lembrando que não são tipos obrigatórios, assim não retorna erro
    resultado = {}

    for nome_produto, valor in produtos.items():
        resultado[nome_produto] = f'{valor * (1 - desconto):.2f}'

    return resultado


valores_produtos = {
    'microondas': 497.99,
    'computador': 3499.97,
    'forno': 399.97
}

print(aplica_desconto(valores_produtos, 0.15))


def aplica_baskhara(a: float, b: float, c: float) -> (float, float):  # Anotação de dicas de tipos
    delta = b ** 2 - 4 * a * c
    x_1 = (- b + (delta ** 1/2)) / (2 * a)
    x_2 = (- b - (delta ** 1/2)) / (2 * a)

    return x_1, x_2


print(aplica_baskhara(5, 15, -25))

x: list = '1,2,3'.split(',')  # Separar string na vírgula. Anotação de dica list, pois retorna uma lista com o valores
print(x)

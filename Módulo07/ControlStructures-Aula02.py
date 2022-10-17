# OPERADORES LÓGICOS
# ==========================
# IS
x = True
y = True

print('*** IS ***')
print(x is y)
print(True is False)

# AND
# | Var. 1 | Var. 2 | Resultado |
# | False  | False  | False     |
# | False  | True   | False     |
# | True   | False  | False     |
# | True   | True   | True      |

print('\n*** AND ***')
print(False and False)
print(False and True)
print(True and False)
print(True and True)

# OR
# | Var. 1 | Var. 2 || Resultado ||
# ---------+--------++-----------||
# | False  | False  || False     ||
# | False  | True   || True      ||
# | True   | False  || True      ||
# | True   | True   || True      ||

print('\n*** OR ***')
print(False or False)
print(False or True)
print(True or False)
print(True or True)

# NOT
print('\n*** NOT ***')
print(not False)
print(not True)

# OPERADORES DE COMPARAÇÃO
# ==========================

print('\n*** OPERADORES DE COMPARAÇÃO ***')

x = 10
y = 20

# ==
print(f'{x} == {y}: {x == y}')

# !=
print(f'{x} != {y}: {x != y}')

# >
print(f'{x} > {y}: {x > y}')

# >=
print(f'{x} >= {y}: {x >= y}')

# <
print(f'{x} < {y}: {x < y}')

# <=
print(f'{x} <= {y}: {x <= y}')

# OPERADORES DE ATRIBUIÇÃO
# ==========================

print('\n*** OPERADORES DE ATRIBUIÇÃO ***')

x = 100

print(f'O valor inicial de x = {x}')

# +=
x += 10
print(f'x += 10 = {(x)}\t(Equivalente: x = x + 10)')

# -=
x -= 5
print(f'x -= 5 = {(x)}\t(Equivalente: x = x - 5)')

# /=
x /= 5
print(f'x /= 5 = {(x)}\t(Equivalente: x = x / 5)')

# *=
x *= 5
print(f'x *= 5 = {(x)}\t(Equivalente: x = x * 5)')

# //=
x //= 20
print(f'x //= 20 = {(x)}\t(Equivalente: x = x // 20)')

# %=
x %= 3
print(f'x %= 3 = {(x)}\t(Equivalente: x = x % 3)')
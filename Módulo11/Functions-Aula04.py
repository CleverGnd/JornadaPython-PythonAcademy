# Funções em Python - Parâmetros Nomeados

def monta_computado(cpu, memoria, hd):
    print('O computador montado foi: ')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memoria} Gb')
    print(f'\tHD: {hd} Tb')


monta_computado('Core i7', 16, 2)  # Argumentos posicionais

monta_computado(memoria=16, hd=2, cpu='Core i7')  # Utilizando parâmetros nomeados, não é necessário a ordem da função

# Parâmetros com valor padrão


def monta_computado(cpu, memoria, hd, monitor=17):

    print('O computador montado foi: ')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memoria} Gb')
    print(f'\tHD: {hd} Tb')
    print(f'\tMonitor: {monitor} "')


monta_computado('Core i7', 16, 2)  # Sem o argumento monitor, retorna o valor padrão
monta_computado('Core i7', 16, 2, 25)  # Passando o parâmetro, a função descarta o valor padrão e retorna o valor informado

# Número de parâmetros variáviveis


def monta_computado(cpu, memoria, hd, monitor=17, **outros_atributos):

    print('O computador montado foi: ')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memoria} Gb')
    print(f'\tHD: {hd} Tb')
    print(f'\tMonitor: {monitor} "')
    print(f'\tOutros atributos: {outros_atributos}')

    # Melhorar o retorno de outros_atributos
    print(f'\tOutros atributos:')
    for chave, valor in outros_atributos.items():
        print(f'\t\t {chave} : {valor}')


monta_computado(memoria=16, hd=2, cpu='Core i7', webcam='Webcam Taz', teclado='Teclado mecânico')
# Adicionando parâmetros, retorna um dicionário com as informações adicionais

# Adicionando parâmetros


def monta_computado(cpu, memoria, hd, *precos, monitor=17, **outros_atributos):

    print('O computador montado foi: ')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memoria} Gb')
    print(f'\tHD: {hd} Tb')
    print(f'\tPreços praticados: {precos}')

    # Melhorando
    print(f'\tPreços praticados:')
    for preco in precos:
        print(f'\t\t R$ {preco:.2f}')

    print(f'\tMonitor: {monitor} "')
    print(f'\tOutros atributos: {outros_atributos}')

    # Melhorar o retorno de outros_atributos
    print(f'\tOutros atributos:')
    for chave, valor in outros_atributos.items():
        print(f'\t\t {chave} : {valor}')


monta_computado('Core i7', 16, 2, 2500, 3199, 4200, monitor=25, webcam='Webcam Taz', teclado='Teclado mecânico')

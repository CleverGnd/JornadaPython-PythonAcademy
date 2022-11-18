# Herança e polimorfismo no Python

from random import randint
from time import sleep

valor_pedagio_carro = 3.5
valor_pedagio_moto = 2.75

valor_km_rodado_carro = 1.5
valor_km_rodado_moto = 1


class Automovel:
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ''
        print(f'Automóvel {self.montadora} {self.modelo} adquitido pela Locadora!')

    def alugar(self, nome_cliente):
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O Automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}!')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O Automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}!')

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):  # Método abstrato, precisa ser implementado
        raise NotImplementedError  # Ainda não implementado


class Carro(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)  # super, pega a classe superior (no caso Automovel)
        print('O automóvel adquirido foi um Carro!')

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * valor_pedagio_carro + valor_km_rodado_carro * km_rodados
        print(f'Fatura do Carro {self.montadora} {self.modelo} '
              f'gerada com sucesso no valor de R$ {self.valor_fatura:.2f}')


class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print('O automóvel adquirido foi um Moto!')

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * valor_pedagio_moto + valor_km_rodado_moto * km_rodados
        print(f'Fatura da Moto {self.montadora} {self.modelo} '
              f'gerada com sucesso no valor de R$ {self.valor_fatura:.2f}')


def mostrar_fatura(automovel):  # Aplicação do polimorfismo no Python
    print(f'O Valor da Fatura do Automóvel {automovel.montadora} {automovel.modelo}'
          f' alugado por {automovel.nome_cliente} ficou no valor de R$ {automovel.valor_fatura:.2f}')

# ------------------------- Aplicação -------------------------

fiesta = Carro('Ford', 'Fiesta', False)
fiesta.alugar('João')

# Simulação tempo aluguel do automóvel
sleep(randint(2, 5))  # Pausa por um valor entre 2 e 5 segundos

fiesta.devolver_automovel()
fiesta.gerar_valor_fatura(numero_pedagios=5, km_rodados=750)
mostrar_fatura(fiesta)

honda_cb = Moto('Honda', 'CB-500', False)
honda_cb.alugar('Ana')

# Simulação tempo aluguel do automóvel
sleep(randint(2, 5))  # Pausa por um valor entre 2 e 5 segundos

honda_cb.gerar_valor_fatura(3, 500)
mostrar_fatura(honda_cb)

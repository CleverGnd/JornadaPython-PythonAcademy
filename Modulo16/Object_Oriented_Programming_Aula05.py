# Atributos e métodos de classe

from random import randint
from time import sleep

valor_pedagio_carro = 3.5
valor_pedagio_moto = 2.75

valor_km_rodado_carro = 1.5
valor_km_rodado_moto = 1


class Automovel:
    numero_total_locacoes = 0  # Atributo de classe, compartilhado entre todas as instancias

    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ''
        print(f'Automóvel {self.montadora} {self.modelo} adquitido pela Locadora!')

    def alugar(self, nome_cliente):
        Automovel.numero_total_locacoes += 1  # Chama classe, atributo e incrementa 1 a este atributo
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O Automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}!')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O Automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}!')

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):  # Método abstrato, precisa ser implementado
        raise NotImplementedError  # Ainda não implementado

    @classmethod  # Método de classe
    def mostrar_numero_total_locacoes(cls):  # cls associando a classe
        print(f'O total de locações de Automóveis é {cls.numero_total_locacoes}')


class Carro(Automovel):
    numero_total_locacoes_carro = 0  # Atributo especifico da classe carro
    valor_total_locacoes = 0.0

    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)  # super, pega a classe superior (no caso Automovel)
        print('O automóvel adquirido foi um Carro!')

    def alugar(self, nome_cliente):
        super(Carro, self).alugar(nome_cliente)
        Carro.numero_total_locacoes_carro += 1

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * valor_pedagio_carro + valor_km_rodado_carro * km_rodados
        print(f'Fatura do Carro {self.montadora} {self.modelo} '
              f'gerada com sucesso no valor de R$ {self.valor_fatura:.2f}')
        Carro.valor_total_locacoes += self.valor_fatura

    @classmethod
    def calcular_media_locacao(cls):
        if cls.numero_total_locacoes_carro != 0:
            media_locacoes = cls.valor_total_locacoes / cls.numero_total_locacoes_carro
            print(f'O valor médio de Locação de Carros está em R$ {media_locacoes}/locação')
        else:
            print('O numero total de Locações de Carro é igual a zero')


class Moto(Automovel):
    numero_total_locacoes_moto = 0
    valor_total_locacoes = 0.0

    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print('O automóvel adquirido foi um Moto!')

    def alugar(self, nome_cliente):
        super(Moto, self).alugar(nome_cliente)
        Moto.numero_total_locacoes_moto += 1

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * valor_pedagio_moto + valor_km_rodado_moto * km_rodados
        print(f'Fatura da Moto {self.montadora} {self.modelo} '
              f'gerada com sucesso no valor de R$ {self.valor_fatura:.2f}')
        Moto.valor_total_locacoes += self.valor_fatura

    @classmethod
    def calcular_media_locacao(cls):
        if cls.numero_total_locacoes_moto != 0:
            media_locacoes = cls.valor_total_locacoes / cls.numero_total_locacoes_moto
            print(f'O valor médio de Locação de Motos está em R$ {media_locacoes}/locação')
        else:
            print('O numero total de Locações de Moto é igual a zero')


def mostrar_fatura(automovel):  # Aplicação do polimorfismo no Python
    print(f'O Valor da Fatura do Automóvel {automovel.montadora} {automovel.modelo}'
          f' alugado por {automovel.nome_cliente} ficou no valor de R$ {automovel.valor_fatura:.2f}')

# ------------------------- Aplicação -------------------------

fiesta = Carro('Ford', 'Fiesta', False)
fiat_mobi = Carro('Fiat', 'Mobi', False)
honda_cb = Moto('Honda', 'CB-500', False)
vw_polo = Carro('Volkswagen', 'Polo', False)

fiesta.alugar('João')

# Pausa 1 segundo
sleep(1)

fiesta.devolver_automovel()
fiesta.gerar_valor_fatura(numero_pedagios=5, km_rodados=750)
mostrar_fatura(fiesta)

fiat_mobi.alugar('Joana')

# Pausa 1 segundo
sleep(1)

fiat_mobi.devolver_automovel()
fiat_mobi.gerar_valor_fatura(2, 250)
mostrar_fatura(fiat_mobi)


honda_cb.alugar('Ana')

# Pausa 1 segundo
sleep(1)

honda_cb.gerar_valor_fatura(3, 500)
mostrar_fatura(honda_cb)

print(f'Total de carros locados {Carro.numero_total_locacoes_carro}')
print(f'Total de motos locadas {Moto.numero_total_locacoes_moto}')

print(Moto.calcular_media_locacao())
print(Carro.calcular_media_locacao())

# Programação orientada a objetos no Python

class Celular:  # Convencionalmente utilizar letra inicial maiúsculo e sem "_"
    # Construtor da classe
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada

    def ligar_tela(self):  # self é o padrão para o primeiro método, referencia a propria instancia
        self.tela_ligada = True


celular_android = Celular("Samsung", "S10", 6.25, 128, 4, 21, 3400, False)  # Instanciação de forma posicional
# Cada argumento é definido em sua posição

# Utilizando o nome do atributo, podemos instancia-lós indiferente da ordem
celular_iphone = Celular(modelo="iPhone 13 PRO", fabricante="Apple", tela=5.75, armazenamento=128, memoria=4,
                         camera=16, bateria=2650, tela_ligada=False)

celular_iphone.ligar_tela()  # Utilizando a função ligar tela

print(celular_iphone.tela_ligada)





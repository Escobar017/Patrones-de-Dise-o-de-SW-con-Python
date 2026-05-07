class carro ():
    def _init_(self, color,marca,modelo,ano):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def arrancar(self):
        print("El carro se ha arrancado")

    def frenar(self):
        print("El carro esta frenando")
    
    def acelelar(self):
        print("El carro esta acelerando")

def make_arrancar(make):
    make.arrancar()

def make_frenar(make):
    make.frenar()

def make_acelelar(make):
    make.acelelar()

carrobmw = carro("Negro", "Mazda", "Mazda 2", 2026)
make_frenar(carrobmw)
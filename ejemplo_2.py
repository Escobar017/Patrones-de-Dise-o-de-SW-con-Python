def make_arrancar(carrovw): #<-- Esta es mi funcion 
    carrovw.arrancar()

class Carro: # <-- Esta es mi clase
    def _init_(self, color, marca, modelo, ano): #<--- Estos son mis atributos
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def arrancar(self): #<--Este es mi metodo
        print("El carro se ha arrancado")

    def frenar(self): #<--Este es mi metodo
        print("El carro se ha frenado")

a = Carro("Negro", "Mazda", "Mazda 2", 2026) #<-- Este es mi objeto
make_arrancar(a)

"""
Una función como make_arrancar:

Recibe un objeto y utiliza sus métodos o atributos sin pertenecer a la clase
"""
"""
Duck Typing --> Es un concepto relacionado con la forma en que algunos lenguajes de programación como Python manejan la tipificación de datos y las llamadas a metodos o propiedades de objetos

El termino proviene de la frase: Si camina ciomo un pato y suena como un poato, entonces debe de ser un pato

En el contexto de la programacion esto significa que no nos preocupamos el tipo real de un objeto, si no más por su comportamiento. Es decir que metodos o propiedades realmente tiene.

"""

def make_it_quack(duck):
    duck.quack()

class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def bark(self):
        print("Woof!")

d = Duck()
make_it_quack(d) #<-- Aqui va imprimir el valor

dog = Dog()
make_it_quack(dog) #<-- Aqui va a tronar

"""
Claro. Se lo dejo resumido, claro y directo del punto 1 al 5:

Resumen del punto 1 al 5
1) Función

La función en su código es:

def make_it_quack(duck):
    duck.quack()
¿Por qué es función?

Porque está fuera de una clase.

👉 Función: make_it_quack()

2) Métodos

Los métodos son los def que están dentro de una clase.

En su código hay 2 métodos:

def quack(self):
    print("Quack!")
def bark(self):
    print("Woof!")

👉 Métodos: quack() y bark()

3) Clases

Las clases son las estructuras que definen el comportamiento de los objetos.

En su código son:

class Duck:
class Dog:

👉 Clases: Duck y Dog

4) Objetos

Los objetos son las instancias creadas a partir de una clase.

En su código:

d = Duck()
dog = Dog()

👉 Objetos: d y dog

5) Resumen general de su código
make_it_quack() → es una función
quack() y bark() → son métodos
Duck y Dog → son clases
d y dog → son objetos
En una sola frase:

Su código tiene una función que recibe un objeto y trata de ejecutar en él un método, dependiendo de la clase a la que pertenezca.

Función: bloque de código que realiza una tarea.
Clase: plantilla para crear objetos.
Objeto: instancia creada a partir de una clase.
Método: función que pertenece a una clase.
"""
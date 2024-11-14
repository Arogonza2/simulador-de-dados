"""
EJERCICIO:
  Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
  atributos y una función que los imprima (teniendo en cuenta las posibilidades
  de tu lenguaje).
  Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
  utilizando su función.
 

"""

class Programer:
    
    def __init__(self, name: str, age: int, languages: list): 
        self.name = name
        self.age = age
        self.languages = languages
        
    def print(self):
        print(f"Nombre: {self.name}" | Edad: {self.age} | Lenguages: {self.languages}")
              
              
my_programer = Programer("Brais", 36, ["Python", "Kotlin","Swift"])
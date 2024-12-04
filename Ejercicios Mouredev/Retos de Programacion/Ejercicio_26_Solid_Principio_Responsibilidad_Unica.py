

from abc import ABC, abstractmethod

"""
EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *

"""

class Form:
    
    def draw(self):
        pass
    

class Square(Form):
    def draw(self):
        print("Dibuja un cuadrado")
        
class Circle(Form):
    def draw(self):
        print("Dibuja un circulo")

class Triangle(Form):
    def draw(self):
        print("Dibuja un triangulo")
        


"""
Extra 

"""


class Operaction(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass
    
class Addition(Operaction):
    def execute(self, a, b):
        return a + b 
    
    
class Substration(Operaction):
    def execute(self, a, b):
        return a - b 
    
class Multiplication(Operaction):
    def execute(self, a, b):
        return a * b 

class Division(Operaction):
    def execute(self, a, b):
        return a // b

class Power(Operaction):
    def execute(self, a, b):
        return a ** b
    
class Calculator:
    def __init__(self) -> None:
        self.operations = {}
    
    def add_operation(self, name, operation):
        self.operations[name] = operation
    
    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f" La operacion {name} no esta soportada ")
        return self.operations[name].execute(a, b)
    

calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())

print(calculator.calculate("addition", 10,5))
print(calculator.calculate("substration", 10, 5))
print(calculator.calculate("multiplication", 10, 5))
print(calculator.calculate("division", 10, 5))
print(calculator.calculate("power", 10, 5))


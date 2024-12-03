


"""
EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 
"""

class Sigleton:
    
    _instace = None

    def __new__(cls):
        if not cls._instace:
            cls._instace = super(Sigleton, cls).__new__(cls)
        
        
        return cls._instace

sigleton1 = Sigleton()
print(sigleton1)

sigleton2 = Sigleton()

print(sigleton2)

print(sigleton1 is sigleton2)
    
    

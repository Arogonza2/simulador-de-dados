"""
 EJERCICIO:
  Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
  operaciones (debes utilizar una estructura que las soporte):
    - Añade un elemento al final.
    - Añade un elemento al principio.
    - Añade varios elementos en bloque al final.
    - Añade varios elementos en bloque en una posición concreta.
    - Elimina un elemento en una posición concreta.
    - Actualiza el valor de un elemento en una posición concreta.
    - Comprueba si un elemento está en un conjunto.
    - Elimina todo el contenido del conjunto.

"""

# Estructura de datos

data = [1, 2, 3, 4, 5]

print(f" Estructura inicial {data}")

data.append(6)
print(f" Añadiendo elemento al final {data}")

data.insert(0, 0)
print(f" Añadiendo elemento al principio {data}")

data.extend([7, 8, 9])
print(f" Añadiendo en bloque al final {data}")

data [3:3]= [-1, -2, -3]
print(f" Añadiendo elementos en una posicion {data}")


del data [3]
print(f" Eliminar un elemento en una posicion{data}")

data[4] = -1
print(f" Actualizando un elemento concreto {data}")

print(f" Comprobar si un elemento existe: {-1 in data}")

print(f" Eliminar el contenido  {data.clear()}")


"""
Extra (Para operar con conjuntos se usan los set{})
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

print(f" Union {set_1.union(set_2)} ")       # Une los conjuntos entre si 

print(f" Interseccion {set_1.intersection(set_2)} ") # Muestra los elementos en comun de los dos conjuntos (set)

print(f" Diferencia {set_1.difference(set_2)} ")   # Muestra el elemento diferente en relacion del set_1 y set_2

print(f" Diferencia {set_2.difference(set_1)} ")   # Muestra el elemento diferente en relacion del set_2 y set_1

print(f" Diferencia {set_1.symmetric_difference(set_2)} ")  # Muestra los elementos diferentes de los dos set 

 







"""
 EJERCICIO:
 
  Muestra ejemplos de creación de todas las estructuras soportadas por defecto
  en tu lenguaje.
  
  Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# Listas 

my_list = ["Brais", "Bl4ck", " Wolfy", "Visionos"]

print(my_list)

my_list.append("Castor") # Insercion

print(my_list)

my_list.remove("Brais") # Eliminacion

print(my_list)

my_list[1] = "Cuervillo" # Actualizacion

print(my_list)

my_list.sort()  # Ordenacion por defecto por orden alfabetico

print(my_list)  


# Tuplas 

my_tuple = ( "Brais", "Moure", "@mouredev" ,"36")  # Las tuplas son inmutables

print(my_tuple[1])    # Acceso
my_tuple = tuple(sorted(my_tuple)) # Ordenacion
print(my_tuple)


 







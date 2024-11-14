"""
* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 
"""

# Opreraciones 

s1 = "Hola"
s2 = " Python"

# Concatenaciones

print( s1 + "," + s2  +"!")

# Repeticiones

print(s1 * 3)

# Indexacion



# Longitud
print(len(s2))

# Slicing (porcion)
print(s2[0:6])

# Busqueda

print("a" in s1)
print("i" in s1)

# Remplazar

print(s1.replace("o", "a"))

# Division 
print(s2.split("t"))

s2 = "Python"

# Mayusculas,  Minusculas y primera letra en mayuscula

print(s1.upper())
print(s1.lower())
print("brais moure".title())
print("brais moure".capitalize())


# Eliminacion de espacios al principio y al final 

print(" Brais moure". strip())

 






 


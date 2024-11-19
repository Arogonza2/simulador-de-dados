"""
 EJERCICIO:
  Desarrolla un programa capaz de crear un archivo que se llame como
  tu usuario de GitHub y tenga la extensión .txt.
  Añade varias líneas en ese fichero:
  - Tu nombre.
  - Edad.
  - Lenguaje de programación favorito.
  Imprime el contenido.
  Borra el fichero.
 
"""

import os

file_name = " alrogon.txt"

with open(file_name, "w") as file:
  file.write("Alfonso Rodriguez\n")
  file.write("36\n")
  file.write("Python")
  


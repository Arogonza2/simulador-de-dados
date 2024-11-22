import re

"""
 EJERCICIO:
  Utilizando tu lenguaje, explora el concepto de expresiones regulares,
  creando una que sea capaz de encontrar y extraer todos los números
  de un texto.

"""

regex = r"\d+"

text = "Este es el ejercicio 16 publicado el 15 /04/2024"

def find_numbers(text: str) -> list:
  return re.findall(regex, text)

print(find_numbers(text))


"""
Extra:
 Crea 3 expresiones regulares (a tu criterio) capaces de:
  - Validar un email.
  - Validar un número de teléfono.
  - Validar una url.
  
"""


# Validar email

def validate_email(email: str)-> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))
  

print(validate_email("piponso@gmail.com"))


#Validar telefono


def validate_phone(phone: str)-> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$",phone ))
  

print(validate_phone("+34 901 23 45 68 "))


# Validar una url

def validate_url(url: str)-> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$",url ))
  

print(validate_url("https://mouredev.com"))




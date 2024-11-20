
from datetime import datetime


"""
 EJERCICIO:
  Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
  - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
  - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
  Calcula cuántos años han transcurrido entre ambas fechas.


"""

now = datetime.now()

birth_date = datetime(1971, 7, 9, 12, 0, 0)

print(now)
print(birth_date)

difference = now - birth_date
print(difference)

print(f" Tengo {difference.days // 365} años.")

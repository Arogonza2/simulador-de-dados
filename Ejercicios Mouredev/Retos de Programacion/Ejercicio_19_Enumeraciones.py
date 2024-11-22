from enum import Enum

"""
EJERCICIO:
  Empleando tu lenguaje, explora la definición del tipo de dato
  que sirva para definir enumeraciones (Enum).
  Crea un Enum que represente los días de la semana del lunes
  al domingo, en ese orden. Con ese enumerado, crea una operación
  que muestre el nombre del día de la semana dependiendo del número entero
  utilizado (del 1 al 7).

"""

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THUSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_day(number:int):
    print(Weekday(number).name)

get_day(1)
get_day(3)


    

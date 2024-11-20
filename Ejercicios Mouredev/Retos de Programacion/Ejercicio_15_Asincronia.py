import datetime
import asyncio

"""
 EJERCICIO:
  Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
    asíncrona una función que tardará en finalizar un número concreto de
    segundos parametrizables. También debes poder asignarle un nombre.
  La función imprime su nombre, cuándo empieza, el tiempo que durará
    su ejecución y cuando finaliza.
 

"""

async def task(name: str, duration: int):
    print(
        f"Tarea: {name}. Duration: {duration}s. Inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(
        f"Tarea: {name}. Fin: {datetime.datetime.now()}")


asyncio.run(task("1", 2))

"""
Extra

"""

async def async_task():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)

asyncio.run(async_task())

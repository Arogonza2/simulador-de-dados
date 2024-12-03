import logging

"""
 EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.

"""

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s ",
                    handlers= [logging.StreamHandler()])
logging.debug(" Esto es un mensaje de DEBUG")
logging.info("Esto es un mendsaje de INFO")
logging.warning("Este es un mensaje de WARNIG")
logging.error("Esto es un mensaje de ERROR")
logging.critical("Esto es un mensaje de CRITICAL")




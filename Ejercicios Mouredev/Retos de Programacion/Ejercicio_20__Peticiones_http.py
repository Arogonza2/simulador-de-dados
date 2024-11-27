import requests

"""
 EJERCICIO:
  Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
   una petición a la web que tú quieras, verifica que dicha petición
   fue exitosa y muestra por consola el contenido de la web.
"""

response = requests.get("https://google.es")
if response.status_code == 200:
    print(response.text)
else: 
    print(f"Error con codigo{response.status_code} al realizar la peticion")




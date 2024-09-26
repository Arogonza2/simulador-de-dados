

"""
Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero

"""

print(f" 4 == 4 = {4 == 4 }")
print(f" 5 != 8 = {5 != 8}")
print(f" 10 > 5 = {10 > 5}")
print(f" 10 >= 5 = {10 >= 5}")

"""
Ejercicio 2

Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario
tiene una longitud mayor o igual que 3 y a su vez es menor que 10 
(es suficiene con mostrar True o False).
"""
a = 5
b = 10


if a == 5 and b ==10:
    print(f"a vale {a} y b vale {b}" )
    


n = 8

if n % 2 == 0:
    print(n, "es un numero par")
else:
    print(n," es un numero impar")
    
    
comando = "SALUDAR"

if comando == "ENTRAR":
    print(" Bien venido al sistema ")
elif comando == "SALUDAR":
    print("Hola, espero que este bien ")
elif comando == "SALIR":
    print("Saliendo del sistema.....")
else:
    print(" Este comando no se reconoce ")


nota = float(input("Introduce una nota: "))

if nota >= 9:
    print( " Has conseguido un: Sobresaliente" )
elif nota >= 7:
    print( " Has conseguido un: Notable" )
elif nota >= 5:
    print(" Has conseguido un: Suficiente ")
else:
    print(" Has conseguido un: Insuficiente")



    


#Operadores aritmeticos

print(f"Suma 10 + 3 = {10 + 3}")
print(f"Resta 10 - 3 = {10 - 3}")
print(f"Multiplicar 10 * 3 = {10 * 3}")
print(f"Division 10 / 3 = {10 / 3}")
print(f"Division entera 10 // 3 = {10 // 3}")
print(f"Modulo 10 % 3 = {10 % 3}")
print(f"Exponente 10 ** 3 = {10 ** 3}")


# Operadores de comparacion

print(f"Igual a 10 == 3 {10 == 3}")
print(f"Distinto a 10 != 3 = {10 != 3}")
print(f"Mayor que  10 > 3 = {10 > 3}")
print(f"Menor que 10 < 3 = {10 < 3}")
print(f"Mayor o menorigual que 10 >= 3 {10 >= 3}")
print(f"Menor o igual que 10 <= 3 {10 <= 3}")

# Operadores logicos
print(f"AND && : 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4 }")
print(f"OR || : 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4 }")       # con uno que sea True el resultado es True
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14  }")


# Operadores de Asignacion

my_numero = 11          # Asigancion
print(my_numero)
my_numero +=  1         # Suma y asignacion 
print(my_numero)
my_numero -= 1          # Resta y asignacion
print(my_numero)
my_numero *= 2          # Multiplicacion y asignacion
print(my_numero)
my_numero /= 2          # Division y asignacion
print(my_numero)
my_numero %= 2          # Modulo y asignacion 
print(my_numero)
my_numero **= 1         # Exponebte y asiognacion
print(my_numero)
my_numero //= 1         # Division entera y asignacion
print(my_numero)

# Operadores de identidad 
my_new_namber = my_numero           # Comprueba si la variable ocupa el mismo lugar de memoria

print(f"my_number is my_new_number es {my_numero is my_new_namber}")
print(f"my_number is not  my_new_number es {my_numero is not my_new_namber}")


# Operaciones de pertenencia

print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' in 'mouredev' = {'b' in 'mouredev'}")

"""
Estructuras de control

"""


# Condicionales 

my_string = "Mouredev"

if my_string == "Mouredev":
    print("mi stringa es 'Mouredev' ")
elif my_string == "Brais":
    print("mi string es 'Brais' ")
else:
    print("mi string no es 'Mouredev' ni 'Brais'")


# Iterables o Iterativas

 
for i in range(11):
    print(i)
i = 0

while i <= 10:
    print(i)
    i += 1


# Manejo de excepciones 

try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
    
    
# Extra

for number in range(10, 56):
    if number % 2 == 0  and number != 16 and number % 3 != 0 :
        print(number)
    

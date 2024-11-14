"""
Funciones y Alcances 

""" 

# Funciones  Simple

def my_greet():
    print("Hola, Python!")

my_greet()


# Funcion con retorno
 
def return_greet():
    return "Hola, Python!" 
 

print(return_greet())  


# Funcion con argumento

def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Brais")
arg_greet("Paco")


# Funcion con argumentos

def args_greet(greet, name):
    print(f"{greet} {name}")

args_greet("Hi", "Brais")


# Funcion con argumento

def defaul_arg_greet(name = "Paco"):
    print(f"Hola, {name}")

defaul_arg_greet()
defaul_arg_greet("Brais")


# Con retorno de varios valores 

def multuple_args_geet():
    return "Hola", "Python!"

greet, name = multuple_args_geet()
print(greet)
print(name)


# Con numero de argumentos variables

def variable_arg_geet(* names):
    for name in names:
        print(f"Hola, {name}!")
        
variable_arg_geet("Python", "Brais", "Paco", "Comunidad")


# Con un numero variable de argumentos con palabra clave


def variable_key_arg_geet(** names):
    for key, value in names.items():
        print(f"{value} ({key})")
        
variable_key_arg_geet(
    language="Python",
    name="Brais",
    alias= "Mouredev",
    age = 36
)

#Funciones dentro de funciones

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python!")
    inner_function()


outer_function()


# Funciones del Lenguaje 

print(len("Alfonso"))
print(type(36))
print("Alfonso".upper())


# Variables Locales y Globales 

global_var = "Python"

print(global_var)

def hello_python():
    local_var = "Hola" # Solo se puede acceder desde dentro de la funcion
    print(f"{local_var}, {global_var}!")


print(global_var) # Se accede desde fuera de la funcion

hello_python()


# Extra "Fizz" "Buzz"

def print_numbers(text_1, text_2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count+= 1
    return count

print(print_numbers("Fizz", "Buzz")) 
   






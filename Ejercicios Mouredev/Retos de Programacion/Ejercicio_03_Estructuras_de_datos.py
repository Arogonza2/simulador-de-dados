"""
 EJERCICIO:
 
  Muestra ejemplos de creación de todas las estructuras soportadas por defecto
  en tu lenguaje.
  
  Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# Listas 

my_list = ["Brais", "Bl4ck", " Wolfy", "Visionos"]

print(my_list)

my_list.append("Castor") # Insercion

print(my_list)

my_list.remove("Brais") # Eliminacion

print(my_list)

my_list[1] = "Cuervillo" # Actualizacion

print(my_list)

my_list.sort()  # Ordenacion por defecto por orden alfabetico

print(my_list)  


# Tuplas 

my_tuple = ( "Brais", "Moure", "@mouredev" ,"36")  # Las tuplas son inmutables

print(my_tuple[1])    # Acceso
my_tuple = tuple(sorted(my_tuple)) # Ordenacion
print(my_tuple)


# Sets

my_set = {"Brais", "Moure", "@mouredev" ,"36"}
print(my_set)
my_set.add("mouredev@gamil.com") # Insercion
print(my_set)
my_set.add("mouredev@gamil.com") # No admite duplicados

my_set.remove ("mouredev@gamil.com")
print(my_set)


# Diccionarios

my_dict = dict ={
  "name": "Brais",
  "surname": "Moure",
  "alias": "@mouredev",
  "age" : "36"
  } 
print(my_dict)

my_dict["email"] = "mouredev@gamil.com"  # Insertar 

print(my_dict)




"""
Extra
"""



def my_agenda():
  
    agenda={}
    
    def insert_contact():
        phone = input("Introduce el telefono de contacto: ")
        if phone.isdigit() and len(phone) >0 and len(phone) <= 11:
            agenda[name]= phone
              
        else:
            print(
                  "Debes introducir un numero de telefono con un maximo de 11 digitos ")
      
  
    while True:
      
        print(" ")     
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
      
      
        option = input("\nSelecciona una opcion: ")
      
        match option:
          
            case "1":
              name = input("Introduce el nombre del contacto a buscar: " )
              if name in agenda:
                  print(
                    f" El numero de telefono de {name} es {agenda[name]}. ")
              
              else:
                  print(f"El contacto {name} no existe. ")
        
          
            case "2":
              name = input("Introduce el nombre del contacto: ")
              insert_contact()
                      
            case "3":
              name = input("Introduce el nombre del contacto a actualizar: " )
              if name in agenda:
                insert_contact()
                        
              else:
                  print(f"El contacto {name} no existe.")
                        
      
            case "4":
              name = input("Introduce el nombre del contacto a eliminar: " )
              if name in agenda:
                del agenda[name]
              
              else:
                  print(f"El contacto {name} no existe.")
            
            
          
            case "5":
                print( "Saliendo de la agenda")
                break
            
            
            case _:
                print("Opcion no valida, selecciona una opcion valida: ")
          
my_agenda()
      
     







"""
EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 * 
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
 
 
"""
class Person:
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.partner = None
        self.children = []
        self.has_parents = False
        
    def add_partner(self, partner):
        if self.partner is not None:
            print(f"{self.name} ya tiene una pareja:{self.partner.name}.")
        else:
            self.partner = partner
            partner.partner = self
            print(f"{self.name} es pareja de {partner.name}.")
            
        
        
    def add_child(self, child):
        if  child not  in self.children:
            self.children.append(child)
            print(f"{self.name} y {self.partner.name} han tenido un hijo: {child.name}.")
        else:
            print(f"{child.name} ya es hijo de {self.name}")
            
class FamilyTree:
    
    def __init__(self):
        self.people = {}
    
    def add_person(self, id , name):
        if id in self.people:
            print(f" La persona con ID {id} ya existe.")
        
        else:
            person = Person(id, name)
            self.people[id] = person
            print(f" La persona con nombre {name}[ID: {id} ha sido añadida al árbol]")
    
    def remove_person(self):
        if id in self.people:
            person = self.people[id]
            del self.people[id]
            print(f" La persona con nombre {person.name} [ID: {id}] ha sido eliminada del arabol ")
        
        else:
            print(f"La persona con ID: {id} no existe en el árbol")
            
            
    def set_partner(self, id1, id2):
        if id1 in self.people and id2 in self.people:
            person1 = self.people[id1]
            person2 = self.people[id2]
            person1.add_partner(person2)
        else:
            print("Algun Id no existe en el árbol.")
        
            
    def add_child(self, parent_id, child_id):
        if parent_id in self.people and child_id in self.people:
            if parent_id == child_id:
                print("Los ID no pueden ser iguales a la hora de asignar un hijo.")
            else:
                parent = self.people[parent_id]
                if parent.partner is None:
                    print(f"Se necesita una pareja para poder tener un hijo.")
                else:
                    child = self.people[child_id]
                    if child.has_parents:
                        print(
                            f"{child.name} [ID: {child.id}] ya tiene padres.")
                    else:
                        child.has_parents = True
                        parent.add_child(child)
                        parent.partner.add_child(child)
        else:
            print("Algún ID no existe en el árbol.")
            
            
    def print_tree(self):
        
        visited = set()

        def print_person(person, level=0):

            if person.id in visited:
                return

            visited.add(person.id)

            indent = "\t" * level

            print(f"{indent} - {person.name} [ID: {person.id}]")

            if person.partner:
                visited.add(person.partner.id)
                print(
                    f"{indent}   Pareja: {person.partner.name} [ID: {person.partner.id}]")

            if person.children:
                print(f"{indent}   Hijos:")
                for child in person.children:
                    print_person(child, level + 1)

        for person in self.people.values():
            is_child = person.has_parents
            if not is_child:
                print_person(person)
        
    
    
tree = FamilyTree()

tree.add_person(1, "Jaime")
tree.add_person(2, "Isidora")

tree.set_partner(1, 2)

tree.add_person(3, "Chari")
tree.add_child(1, 3)
tree.add_person(4, "Goyo")
tree.set_partner(3, 4)



tree.add_person(5, "Paco")
tree.add_child(1, 5)
tree.add_person(6, "Jaime JR")
tree.add_child(1, 6)
tree.add_person(33, "None")
tree.set_partner(6, 33)
tree.add_person(7, "Paloma")
tree.add_child(1, 7)
tree.add_person(8, "Chule")
tree.set_partner(8, 7)
tree.add_person(9, "Jesus")
tree.add_child(1, 9)
tree.add_person(10, "Teresa")
tree.set_partner(9, 10)
tree.add_person(11, "Alfonso")
tree.add_person(12, "Martha")
tree.set_partner(11, 12)
tree.add_child(1, 11)
tree.add_person(13, "Jose")
tree.add_child(1, 13)
tree.add_person(14, " Sara")
tree.set_partner(13, 14)
tree.add_person(15, "Juan Carlos")
tree.add_child(1, 15)
tree.add_person(16, "Nadia")
tree.set_partner(15, 16)
tree.add_person(17, "David")
tree.add_child(1, 17)
tree.add_person(18, "Arantxa")
tree.add_child(3, 18)
tree.add_person(34, "None")
tree.set_partner(18, 34)
tree.add_person(19, "Tamara")
tree.add_child(3, 19)
tree.add_person(20, "Roberto")
tree.add_child(3, 20)
tree.add_person(21, "Jenni")
tree.add_child(18, 21)
tree.add_person(22, "Cristian")
tree.add_child(18, 22)
tree.add_person(23, "Abel")
tree.add_child(18, 23)
tree.add_person(24, "Sara")
tree.add_child(6, 24)
tree.add_person(25, "KIKO")
tree.set_partner(24, 25)
tree.add_person(26, "Manuel")
tree.add_child(24, 26)
tree.add_person(27, "Javi")
tree.add_child(24, 27)
tree.add_person(28, "Chema")
tree.add_child(7, 28)
tree.add_person(29, "Mabel")
tree.add_child(9, 29)
tree.add_person(30, "Jesus JR")
tree.add_child(9, 30)
tree.add_person(31, "Mariana")
tree.add_child(15, 31)
tree.add_person(32, "Adrian")
tree.add_child(15, 32)
tree.add_person(35, "Sara")
tree.add_child(13, 35)
tree.add_person(36, "Angel")
tree.add_child(13, 36)
tree.add_person(37, "Lucia")
tree.set_partner(37, 28)







tree.print_tree()

"""
EJERCICIO:

 Implementa los mecanismos de introducción y recuperación de elementos propios de las
 pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 o lista (dependiendo de las posibilidades de tu lenguaje).

"""

# Pilas / Stack (LIFO) " Ultimo en entrar primero en salir"

stack = []

# push (apilar)

stack.append("1")
stack.append("2")
stack.append("3")

print(stack)

# pop (desapilar)

stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]

print(stack_item)

print(stack.pop())
print(stack)


# Cola / queue (FIFO) "Primero en entrar primero en salir"

queue = []

# enqueue (encolar)

queue.append("1")
queue.append("2")
queue.append("3")

print(queue)

# dequeue (desencolar)

queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))
print(queue)

  


"""

DIFICULTAD EXTRA (opcional):
 - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
    de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
    que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.


"""


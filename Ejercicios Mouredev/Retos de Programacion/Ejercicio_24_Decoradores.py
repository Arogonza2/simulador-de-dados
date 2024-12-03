"""
EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.

"""


def print_call(function):
    def print_function():
        print(f"La funcion '{function.__name__}' ha sido llammada")
        return function
    return print_function


@print_call
def example_function():
    pass    

@print_call
def example_function_2():
    pass

@print_call
def example_function_3():
    pass



example_function()
example_function_2()
example_function_3()


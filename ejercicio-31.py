# Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. 
# Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

# Defino la función que busca un nombre en una lista y lanza una excepción si no lo encuentra.
def buscar_nombre(lista_nombres, nombre):

    # Compruebo si el nombre está en la lista.
    if nombre in lista_nombres:
        print("El nombre '" + nombre + "' se ha encontrado en la lista.")
    else:
        raise ValueError("El nombre '" + nombre + "' no se ha encontrado en la lista.")

# Pido al usuario que introduzca los nombres separados por comas.
entrada = input("Escribe los nombres separados por comas: ")

# Separo los nombres por comas y elimino los espacios en blanco de cada uno.
lista_nombres = [nombre.strip() for nombre in entrada.split(",")]

# Pido al usuario el nombre que quiere buscar.
nombre_buscado = input("Introduce el nombre a buscar: ").strip()

# Llamo a la función y manejo la excepción si el nombre no se encuentra.
try:
    buscar_nombre(lista_nombres, nombre_buscado)
except ValueError as error:
    print(error)
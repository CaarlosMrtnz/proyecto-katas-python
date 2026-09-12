# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# Defino la función que busca el primer elemento duplicado en una lista.
def primer_duplicado(lista):

    # Creo una lista vacía para guardar los elementos no duplicados.
    vistos = []

    # Recorro cada elemento de la lista.
    for elemento in lista:

        # Compruebo si el elemento ya estaba en la lista de vistos.
        if elemento in vistos:
            return elemento

        # Si no, lo añado a la lista de vistos.
        vistos.append(elemento)

    # Si no hay duplicados, devuelvo None.
    return None

# Uso la función con una lista de ejemplo y muestro el resultado por terminal.
numeros = [3, 1, 4, 2, 5, 1, 7, 4]
resultado = primer_duplicado(numeros)
print(resultado)
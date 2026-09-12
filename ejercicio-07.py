# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

# Defino la función que convierte una lista de tuplas a una lista de strings.
def tuplas_a_strings(lista_tuplas):

    # Uso map() con una lambda que convierte cada tupla en string.
    resultado = map(lambda tupla: str(tupla), lista_tuplas)

    # Convierto el resultado de map() en una lista y la devuelvo.
    return list(resultado)

# Creo una lista de tuplas de ejemplo.
tuplas = [(1, 2), (3, 4), (5, 6)]

# Llamo a la función y muestro el resultado por terminal.
lista_strings = tuplas_a_strings(tuplas)
print(lista_strings)
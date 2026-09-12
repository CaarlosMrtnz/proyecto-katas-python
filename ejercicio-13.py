# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
# Las letras no pueden estar repetidas. 
# Usa la función map().

# Defino la función que genera las tuplas de mayúsculas y minúsculas.
def letras_mayusculas_minusculas(caracteres):

    # Elimino las letras repetidas usando un conjunto (set).
    sin_repetidos = set(caracteres)

    # Uso map() con una lambda que crea una tupla con la letra en mayúsculas y minúsculas.
    resultado = map(lambda letra: (letra.upper(), letra.lower()), sin_repetidos)

    # Convierto el resultado de map() en una lista y la devuelvo.
    return list(resultado)

# Uso la función con un conjunto de caracteres de ejemplo y muestro el resultado por terminal.
caracteres = ["a", "b", "c", "a", "d", "b"]
tuplas = letras_mayusculas_minusculas(caracteres)
print(tuplas)
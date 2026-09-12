# Crea una función que cuente el número de caracteres en una cadena de texto dada.

# Defino la función que cuenta los caracteres de una cadena de texto.
def contar_caracteres(texto):

    # Cuento el número de caracteres usando len() y devuelvo el resultado.
    return len(texto)

# Uso la función con una cadena de ejemplo y muestro el resultado por terminal.
cadena = "Me llamo Carlos"
total = contar_caracteres(cadena)
print(total)
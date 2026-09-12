# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas 
# las palabras que sean más largas que n. 
# Usa la función filter().

# Defino la función que filtra las palabras más largas que n.
def palabras_mas_largas(texto, n):

    # Separo el texto en una lista de palabras.
    palabras = texto.split()

    # Uso filter() con una lambda que comprueba si la palabra tiene más de n caracteres.
    resultado = filter(lambda palabra: len(palabra) > n, palabras)

    # Convierto el resultado de filter() en una lista y la devuelvo.
    return list(resultado)

# Uso la función con un texto de ejemplo y muestro el resultado por terminal.
texto = "El lenguaje de programación Python es muy popular entre los desarrolladores"
n = 5
palabras_largas = palabras_mas_largas(texto, n)
print(palabras_largas)
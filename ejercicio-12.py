# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. 
# Usa la función map().

# Defino la función que calcula la longitud de cada palabra de una frase.
def longitud_palabras(frase):

    # Separo la frase en una lista de palabras.
    palabras = frase.split()

    # Uso map() con una lambda que calcula la longitud de cada palabra.
    resultado = map(lambda palabra: len(palabra), palabras)

    # Convierto el resultado de map() en una lista y la devuelvo.
    return list(resultado)

# Uso la función con una frase de ejemplo y muestro el resultado por terminal.
frase = "Hola me llamo Python y soy un lenguaje de programación"
longitudes = longitud_palabras(frase)
print(longitudes)
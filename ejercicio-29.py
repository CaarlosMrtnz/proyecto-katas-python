# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' 
# excepto los últimos cuatro.

# Defino la función que enmascara todos los caracteres excepto los últimos cuatro.
def enmascarar(valor):

    # Convierto el valor a cadena de texto.
    texto = str(valor)

    # La cadena enmascarada repitiendo '#' para todos los caracteres menos los últimos cuatro.
    mascara = "#" * (len(texto) - 4) + texto[-4:]

    # Devuelvo la cadena enmascarada.
    return mascara

# Uso la función con un número de tarjeta de ejemplo y muestro el resultado por terminal.
numero_tarjeta = 1234567890123456
resultado = enmascarar(numero_tarjeta)
print(resultado)
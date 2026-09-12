# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

# Creo la función que recibirá la cadena de texto.
def contar_letras(texto):
    # Diccionario que guarda las letras y sus frecuencias.
    frecuencias = {}

    # Recorrido del texto por carácter.
    for letra in texto:
        # Comprobación de que el carácter no sea un espacio.
        if letra != " ":
            # Si la letra ya está en el diccionario, aumenta su frecuencia.
            if letra in frecuencias:
                frecuencias[letra] += 1
            # Si no está, se añade con una frecuencia inicial de 1.
            else:
                frecuencias[letra] = 1

    # Se termina la función recogiendo el diccionario con el resultado.
    return frecuencias


# Pruebo la función con una cadena de texto y un print para verlo por terminal.
resultado = contar_letras("hola mundo")
print(resultado)


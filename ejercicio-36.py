# Crea una función llamada procesar_texto
    # Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
    # Código a seguir:
        #   a. Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
        #   b. Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
        #   c. Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
        #   d. Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
    # Caso de uso:
        # Verificar el funcionamiento completo de procesar_texto.

# Defino la función que cuenta cuántas veces aparece cada palabra en el texto.
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

# Defino la función que reemplaza una palabra por otra en el texto.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# Defino la función que elimina todas las apariciones de una palabra en el texto.
def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)

# Defino la función principal que gestiona las tres opciones según el argumento recibido.
def procesar_texto(texto, opcion, *args):

    # Compruebo qué opción se ha elegido y llamo a la función correspondiente.
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Esa opción no es válida."
 
# Caso de uso: verifico el funcionamiento completo de procesar_texto.
texto = "me llamo carlos no me llamo david"

# Cuento las palabras del texto.
print(procesar_texto(texto, "contar"))

# Reemplazo una palabra por otra.
print(procesar_texto(texto, "reemplazar", "llamo", "llamaré"))

# Elimino una palabra del texto.
print(procesar_texto(texto, "eliminar", "no"))

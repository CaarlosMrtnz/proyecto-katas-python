# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# Creo una función que recibe una lista de palabras y una palabra objetivo.
def buscar_palabras(lista_palabras, palabra_objetivo):
    # Una lista vacía para guardar las coincidencias.
    palabras_encontradas = []

    # Recorro todas las palabras de la lista mediante for-in.
    for palabra in lista_palabras:
        # Compruebo si la palabra objetivo está dentro de la palabra actual.
        if palabra_objetivo in palabra:
            # Si está, añado la palabra a la lista de resultados.
            palabras_encontradas.append(palabra)

    # Devuelvo la lista de palabras que contienen la palabra objetivo.
    return palabras_encontradas


# Una lista de palabras para probar la función.
palabras = ["casa", "casco", "perro", "casamiento", "gato"]

# Llamada a la función buscando las palabras que contienen "cas".
resultado = buscar_palabras(palabras, "cas")

# Muestro el resultado.
print(resultado)
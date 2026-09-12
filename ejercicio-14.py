# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

# Defino la función que filtra las palabras que empiezan por una letra concreta.
def palabras_por_letra(lista_palabras, letra):

    # Uso filter() con una lambda que comprueba si la palabra empieza por la letra indicada.
    resultado = filter(lambda palabra: palabra.startswith(letra), lista_palabras)

    # Convierto el resultado de filter() en una lista y la devuelvo.
    return list(resultado)

# Creo una lista de palabras de ejemplo y llamo a la función con la letra buscada.
palabras = ["manzana", "melón", "pera", "mango", "plátano", "mandarina"]
letra_buscada = "m"
palabras_filtradas = palabras_por_letra(palabras, letra_buscada)

# Muestro el resultado por terminal.
print(palabras_filtradas)
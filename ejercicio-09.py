# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo 
# ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. 
# Usa la función filter().

# Defino la lista de mascotas prohibidas en España.
mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

# Creo la función que filtra las mascotas no permitidas.
def filtrar_mascotas(lista_mascotas):

    # Con filter() compruebo si la mascota no está en la lista de prohibidas.
    resultado = filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas)

    # Convierto el resultado en una lista y la devuelvo.
    return list(resultado)

# Una lista de mascotas de ejemplo.
mascotas = ["Perro", "Gato", "Mapache", "Conejo", "Tigre", "Serpiente Pitón", "Hámster"]

# Llamo a la función y muestro el resultado por terminal.
mascotas_permitidas = filtrar_mascotas(mascotas)
print(mascotas_permitidas)
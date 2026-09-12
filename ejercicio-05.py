# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. 
# Si es así, el estado será "aprobado"; de lo contrario, "suspenso". 
# La función debe devolver una tupla que contenga la media y el estado.

# Defino la función con la lista de notas y el parámetro opcional nota_aprobado.
def calcular_media_y_estado(notas, nota_aprobado=5):

    # Sumo todos los valores de la lista.
    suma = sum(notas)

    # Calculo la media dividiendo la suma entre el número de elementos.
    media = suma / len(notas)

    # Compruebo si la media es mayor o igual que la nota mínima para aprobar.
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    # Devuelvo la media y el estado como una tupla.
    return (media, estado)

# Un ejemplo.
notas = [6, 7, 4, 8, 5]
resultado = calcular_media_y_estado(notas)
print(resultado)

# Otro ejemplo con una nota de corte diferente.
notas2 = [3, 4, 2, 5]
resultado2 = calcular_media_y_estado(notas2, nota_aprobado=6)
print(resultado2)
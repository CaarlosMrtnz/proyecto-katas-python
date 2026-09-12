# Crea una función que calcule el promedio de una lista de números.

# Defino la función que calcula el promedio de una lista de números.
def calcular_promedio(numeros):

    # Sumo todos los valores y divido entre el número de elementos.
    suma = sum(numeros)
    promedio = suma / len(numeros)

    return promedio

# Uso la función con una lista de ejemplo y muestro el resultado por terminal.
numeros = [10, 20, 30, 40, 50]
resultado = calcular_promedio(numeros)
print(resultado)
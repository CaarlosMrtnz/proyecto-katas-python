# Escribe una función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# Defino la excepción personalizada para listas vacías.
class ListaVaciaError(Exception):
    pass

# Defino la función que calcula el promedio de una lista de números.
def calcular_promedio(numeros):

    # Compruebo si la lista está vacía y lanzo una excepción personalizada.
    if len(numeros) == 0:
        raise ListaVaciaError("La lista no puede estar vacía.")

    # Sumo todos los valores y divido entre el número de elementos.
    suma = sum(numeros)
    promedio = suma / len(numeros)

    return promedio

# Uso la función con un ejemplo y manejo el error si se lanza la excepción.
try:
    numeros = [4, 8, 6, 10, 2]
    resultado = calcular_promedio(numeros)
    print("El promedio es:", resultado)

except ListaVaciaError as error:
    print("Error:", error)
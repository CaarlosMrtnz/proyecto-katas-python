# Escribe una función que calcule el factorial de un número de manera recursiva.

# Defino la función recursiva para calcular el factorial.
def factorial(numero):

    # Compruebo si el factorial de 0 o 1 es 1.
    if numero == 0 or numero == 1:
        return 1

    # En caso recursivo, multiplico el número por el factorial del número anterior.
    return numero * factorial(numero - 1)

# Uso la función con un número de ejemplo y muestro el resultado por terminal.
numero = 5
resultado = factorial(numero)
print(resultado)
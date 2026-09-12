# Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

# Creo una lista de números de ejemplo.
numeros = [100, 20, 10, 5, 3]

# Uso reduce() con una lambda que resta el número actual al acumulado.
diferencia = reduce(lambda acumulado, numero: acumulado - numero, numeros)

# Muestro el resultado por terminal.
print(diferencia)
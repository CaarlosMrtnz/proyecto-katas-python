# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

from functools import reduce

# Creo una lista de números de ejemplo.
numeros = [1, 2, 3, 4, 5]

# Uso reduce() con una lambda que multiplica el acumulado por cada número.
producto = reduce(lambda acumulado, numero: acumulado * numero, numeros)

# Muestro el resultado por terminal.
print(producto)
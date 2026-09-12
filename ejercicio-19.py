# Crea una función lambda que filtre los números impares de una lista dada.

# Creo la función lambda que comprueba si un número es impar.
es_impar = lambda numero: numero % 2 != 0

# Una lista de números de ejemplo.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Uso filter() con la lambda para quedarme solo con los números impares.
resultado = filter(es_impar, numeros)

# Convierto el resultado en una lista y lo muestro por terminal.
numeros_impares = list(resultado)
print(numeros_impares)
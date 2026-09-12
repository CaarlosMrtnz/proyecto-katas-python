# Concatena una lista de palabras. 
# Usa la función reduce().

from functools import reduce

# Una lista de palabras de ejemplo.
palabras = ["Buenas!", " ", "Probando", " ", "reduce", " "]

# Uso reduce() con una lambda que va uniendo cada palabra con la anterior.
resultado = reduce(lambda acumulado, palabra: acumulado + palabra, palabras)

# Muestro el resultado por terminal.
print(resultado)
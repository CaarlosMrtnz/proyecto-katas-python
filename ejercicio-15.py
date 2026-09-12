# Crea una función lambda que sume 3 a cada número de una lista dada.

# Creo la función lambda que suma 3 a un número.
sumar_tres = lambda numero: numero + 3

# Una lista de números de ejemplo.
numeros = [1, 2, 3, 4, 5]

# Aplico la lambda a cada elemento de la lista usando map().
resultado = map(sumar_tres, numeros)

# Convierto el resultado en una lista y lo muestro por terminal.
lista_resultado = list(resultado)
print(lista_resultado)
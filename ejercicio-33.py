# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# Dos listas de números de ejemplo.
lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

# Uso map() con una lambda que suma los elementos en la misma posición de ambas listas.
resultado = map(lambda a, b: a + b, lista1, lista2)

# Convierto el resultado de map() en una lista y lo muestro por terminal.
lista_sumas = list(resultado)
print(lista_sumas)
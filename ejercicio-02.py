# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

# Creo una lista de números.
numeros = [1, 2, 3, 4, 5]

# Uso map() para aplicar una función a cada número.
# La función lambda multiplica cada valor por 2.
numeros_dobles = map(lambda numero: numero * 2, numeros)

# Convierto el resultado de map() en una lista y los muestro mediante print por terminal.
lista_dobles = list(numeros_dobles)
print(lista_dobles)
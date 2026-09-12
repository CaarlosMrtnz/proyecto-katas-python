# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

# Creo una función que recibe dos valores y devuelve su diferencia.
def calcular_diferencia(a, b):
    return a - b

# Dos listas de números para hacer la prueba.
lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 5, 10, 15, 25]

# Uso map() para aplicar la función a cada par de valores de ambas listas.
# map() puede recibir varias listas y pasa un elemento de cada una a la función.
diferencias = map(calcular_diferencia, lista1, lista2)

# Convierto el resultado de map() en una lista y lo muestro mediante print por terminal.
lista_diferencias = list(diferencias)
print(lista_diferencias)
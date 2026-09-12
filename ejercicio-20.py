# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. 
# Usa la función filter().

# Una lista con elementos de tipo integer y string mezclados.
elementos = [1, "hola", 2, "mundo", 3, "python", 4, 5, "programación"]

# Uso filter() con una lambda que comprueba si el elemento es de tipo int.
resultado = filter(lambda elemento: type(elemento) == int, elementos)

# Convierto el resultado de filter() en una lista y lo muestro por terminal.
solo_enteros = list(resultado)
print(solo_enteros)
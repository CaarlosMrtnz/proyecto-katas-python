# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número 572. 
# Usa la función reduce().

from functools import reduce

# Defino la función que convierte una lista de dígitos en un número.
def digitos_a_numero(digitos):

    # Uso reduce() con una lambda que va construyendo el número desplazando los dígitos a la izquierda.
    resultado = reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)

    # Devuelvo el resultado.
    return resultado

# Uso la función con una lista de dígitos de ejemplo y muestro el resultado por terminal.
digitos = [5, 7, 2]
numero = digitos_a_numero(digitos)
print(numero)
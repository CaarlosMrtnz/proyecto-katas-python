# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y 
# datos (una tupla con los datos necesarios para calcular el área de la figura).

# Importo el módulo math para usar el valor de pi en el cálculo del círculo.
import math

# Defino la función que calcula el área según la figura y los datos recibidos.
def calcular_area(figura, datos):

    # Compruebo qué figura se ha indicado y calculo su área.
    if figura == "rectangulo":
        # El área del rectángulo es base por altura.
        area = datos[0] * datos[1]

    elif figura == "circulo":
        # El área del círculo es pi por el radio al cuadrado.
        area = math.pi * datos[0] ** 2

    elif figura == "triangulo":
        # El área del triángulo es base por altura dividido entre dos.
        area = (datos[0] * datos[1]) / 2

    else:
        return "Figura no reconocida."

    return area

# Uso la función con ejemplos de cada figura y muestro los resultados por terminal.
print(calcular_area("rectangulo", (5, 3)))
print(calcular_area("circulo", (4,)))
print(calcular_area("triangulo", (6, 8)))
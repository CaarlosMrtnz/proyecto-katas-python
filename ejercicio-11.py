# Escribe un programa que pida al usuario que introduzca su edad. 
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), 
# maneja las excepciones adecuadamente.

# Pido al usuario que introduzca su edad.
edad_texto = input("Introduce tu edad: ")

# Intento convertir el valor y comprobar si está dentro del rango válido.
try:
    # Convierto el valor introducido a número entero.
    edad = int(edad_texto)

    # Compruebo si la edad está fuera del rango esperado.
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120.")

    # Muestro la edad si es válida.
    print("Tu edad es:", edad)

except ValueError:
    # Capturo el error si el valor no es numérico o está fuera de rango.
    print("Error: el valor introducido no es válido. Introduce un número entre 0 y 120.")
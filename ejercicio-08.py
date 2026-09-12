# Escribe un programa que pida al usuario dos números e intente dividirlos. 
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y 
# muestra un mensaje indicando si la división fue exitosa o no.

# Intento convertir los valores y realizar la división.
try:
    # Pido los dos números al usuario y convierto los valores introducidos a números decimales.
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    
    # Divido los números.
    resultado = numero1 / numero2

    # Muestro el resultado si la división fue exitosa.
    print("La división fue exitosa. Resultado:", resultado)

except (ValueError, ZeroDivisionError):
    # Capturo el error si el usuario introduce un valor no numérico o intenta dividir por cero.
    print("Los valores introducidos deben ser números y el divisor no puede ser cero. Inténtalo de nuevo.")
    

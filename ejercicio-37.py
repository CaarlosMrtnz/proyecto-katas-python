# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

# Pido al usuario que introduzca la hora.
hora = int(input("Introduce una hora (0-23): "))

# Compruebo en qué franja horaria se encuentra la hora introducida.
if hora >= 6 and hora < 12:
    print("Es de día.")
elif hora >= 12 and hora < 21:
    print("Es por la tarde.")
else:
    print("Es de noche.")
# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
# Reglas:
#   0 - 69: insuficiente
#   70 - 79: bien
#   80 - 89: muy bien
#   90 - 100: excelente

# Pido al usuario que introduzca la calificación numérica del alumno.
calificacion = int(input("Introduce la calificación del alumno (0-100): "))

# Compruebo en qué rango se encuentra la calificación y muestro el resultado por terminal.
if calificacion >= 0 and calificacion <= 69:
    print("Insuficiente")
elif calificacion >= 70 and calificacion <= 79:
    print("Bien")
elif calificacion >= 80 and calificacion <= 89:
    print("Muy bien")
elif calificacion >= 90 and calificacion <= 100:
    print("Excelente")
else:
    print("Calificación no válida.")
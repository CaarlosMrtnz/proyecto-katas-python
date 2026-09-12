# Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, 
# calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

# Una lista de diccionarios con información de estudiantes.
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 78},
    {"nombre": "María", "edad": 21, "calificacion": 90},
    {"nombre": "Carlos", "edad": 23, "calificacion": 85},
    {"nombre": "Laura", "edad": 20, "calificacion": 92},
]

# Uso filter() con una lambda que comprueba si la calificación es mayor o igual a 90.
resultado = filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)

# Convierto el resultado de filter() en una lista y lo muestro por terminal.
estudiantes_aprobados = list(resultado)
print(estudiantes_aprobados)
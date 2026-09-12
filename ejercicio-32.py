# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el 
# puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# Una lista de empleados con su nombre completo y puesto.
empleados = [
    {"nombre": "Ana García", "puesto": "Directora"},
    {"nombre": "Luis Martínez", "puesto": "Desarrollador"},
    {"nombre": "María López", "puesto": "Diseñadora"},
    {"nombre": "Carlos Sánchez", "puesto": "Analista"},
]

# Defino la función que busca el nombre en la lista y devuelve el puesto.
def buscar_empleado(nombre_completo, lista_empleados):

    # Recorro la lista de empleados buscando el nombre.
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]

    # Si no encuentro el nombre, devuelvo un mensaje informativo.
    return "La persona no trabaja aquí."

# Uso la función con un nombre de ejemplo y muestro el resultado por terminal.
nombre = "Luis Martínez"
resultado = buscar_empleado(nombre, empleados)
print(resultado)

nombre = "Luis González"
resultado = buscar_empleado(nombre, empleados)
print(resultado)
# Crea la clase Arbol
    # Define un árbol genérico con un tronco y ramas como atributos.
    # Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
    # Código a seguir:
        #   a. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        #   b. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
        #   c. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
        #   d. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
        #   e. Implementar el método quitar_rama para eliminar una rama en una posición específica.
        #   f. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
    # Caso de uso:
        #   a. Crear un árbol.
        #   b. Hacer crecer el tronco una unidad.
        #   c. Añadir una nueva rama.
        #   d. Hacer crecer todas las ramas una unidad.
        #   e. Añadir dos nuevas ramas.
        #   f. Retirar la rama situada en la posición 2.
        #   g. Obtener información sobre el árbol.


# Defino la clase Arbol con sus atributos y métodos.
class Arbol:

    # Inicializo el árbol con un tronco de longitud 1 y una lista vacía de ramas.
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # Aumento la longitud del tronco en una unidad.
    def crecer_tronco(self):
        self.tronco += 1

    # Añado una nueva rama de longitud 1 a la lista de ramas.
    def nueva_rama(self):
        self.ramas.append(1)

    # Aumento en una unidad la longitud de todas las ramas existentes.
    def crecer_rama(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    # Elimino la rama en la posición indicada.
    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    # Devuelvo información sobre el árbol por terminal.
    def info_arbol(self):
        print("Longitud del tronco:", self.tronco)
        print("Número de ramas:", len(self.ramas))
        print("Longitudes de las ramas:", self.ramas)


# Sigo el caso de uso indicado en el enunciado.

# a. Creo un árbol.
arbol = Arbol()

# b. Hago crecer el tronco una unidad.
arbol.crecer_tronco()

# c. Añado una nueva rama.
arbol.nueva_rama()

# d. Hago crecer todas las ramas una unidad.
arbol.crecer_rama()

# e. Añado dos nuevas ramas.
arbol.nueva_rama()
arbol.nueva_rama()

# f. Retiro la rama situada en la posición 2.
arbol.quitar_rama(2)

# g. Obtengo la información sobre el árbol.
arbol.info_arbol()
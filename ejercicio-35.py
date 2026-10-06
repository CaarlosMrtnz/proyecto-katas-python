# Crea la clase UsuarioBanco
    # Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
    # Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
    # Código a seguir:
        #   a. Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
        #   b. Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
        #   c. Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
        #   d. Implementar agregar_dinero para aumentar el saldo del usuario.
    # Caso de uso:
        #   a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
        #   b. Agregar 20 unidades al saldo de Bob.
        #   c. Transferir 80 unidades de Bob a Alicia.
        #   d. Retirar 50 unidades del saldo de Alicia.

# Defino la clase UsuarioBanco con sus atributos y métodos.
class UsuarioBanco:

    # Inicializo el usuario con nombre, saldo y tipo de cuenta.
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # Retiro dinero del saldo y lanzo un error si no hay suficiente.
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para retirar " + str(cantidad) + " unidades.")
        self.saldo -= cantidad
        print(self.nombre + " retiró " + str(cantidad) + ". Saldo actual: " + str(self.saldo))

    # Transfiero dinero desde otro usuario, lanzando un error si el origen no tiene saldo suficiente.
    def transferir_dinero(self, origen, cantidad):
        if cantidad > origen.saldo:
            raise ValueError("El usuario " + origen.nombre + " no tiene saldo suficiente para transferir.")
        origen.saldo -= cantidad
        self.saldo += cantidad
        print(origen.nombre + " transfirió " + str(cantidad) + " a " + self.nombre + ".")

    # Ingreso dinero en el saldo del usuario con la cantidad indicada.
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print("Se han añadido " + str(cantidad) + " unidades a " + self.nombre + ". Saldo actual: " + str(self.saldo))

# Ahora, paso a los casos de uso indicados en el enunciado.

try:  
    # a. Creo dos usuarios con sus saldos iniciales.
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    
    # b. Agrego 20 unidades al saldo de Bob.
    bob.agregar_dinero(20)

    """ El ejercicio se plantea para que salte el error y ver cómo se maneja. La siguiente línea que agrega 30 unidades adicionales al saldo de Bob sirve para poder ejecutar el resto de acciones. Elimna la almohadilla siguiente y se verá un resultado diferente. """
    # bob.agregar_dinero(30) 

    # c. Transfiero 80 unidades de Bob a Alicia.
    alicia.transferir_dinero(bob, 80)

    # d. Retiro 50 unidades del saldo de Alicia.
    alicia.retirar_dinero(50)

except ValueError as e:
    print(e)
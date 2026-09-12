# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en 
# línea, después de aplicar un descuento. El programa debe:
    #   a. Solicitar al usuario el precio original de un artículo.
    #   b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    #   c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    #   d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    #   e. Mostrar el precio final de la compra, considerando o no el descuento.
    #   f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.

# a. Solicito al usuario el precio original del artículo.
precio = float(input("Introduce el precio original del artículo: "))

# b. Pregunto si el usuario tiene un cupón de descuento.
tiene_cupon = str(input("¿Tienes un cupón de descuento? (sí/no): ")).lower().strip()

# Compruebo si el usuario respondió que sí tiene cupón.
if tiene_cupon == "sí" or tiene_cupon == "si":

    # c. Solicito el valor del cupón de descuento.
    descuento = float(input("Introduce el valor del cupón de descuento: "))

    # d. Aplico el descuento solo si el valor es mayor a cero.
    if descuento > 0:
        precio_final = precio - descuento

        # Compruebo que el precio no quede por debajo de cero.
        if precio_final < 0:
            precio_final = 0

        # e. Muestro el precio final con el descuento aplicado.
        print("Precio final con descuento:", precio_final)
    else:
        print("El cupón no es válido. Precio final:", precio)

elif tiene_cupon == "no":

    # e. Muestro el precio final sin descuento.
    print("Precio final sin descuento:", precio)

else:
    print("Debes introducir 'sí' o 'no'.")
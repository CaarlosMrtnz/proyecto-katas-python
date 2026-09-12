# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
# pero en diferente orden.

# Defino la función que comprueba si dos palabras son anagramas.
def comprobar_anagramas(palabra1, palabra2):

    # Convierto ambas palabras a minúsculas para evitar diferencias por mayúsculas.
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Ordeno las letras de cada palabra y compruebo si son iguales.
    return sorted(palabra1) == sorted(palabra2)

# Uso la función con varias palabras de ejemplo y muestro el resultado por terminal.
palabra1 = "amor"
palabra2 = "Roma"
resultado = comprobar_anagramas(palabra1, palabra2)
print(f"¿Las palabras {palabra1} y {palabra2} son anagramas?: {resultado}")

palabra1 = "casa"
palabra2 = "rata"
resultado = comprobar_anagramas(palabra1, palabra2)
print(f"¿Las palabras {palabra1} y {palabra2} son anagramas?: {resultado}")
# Actividad 2 - Organización de datos en ficheros
import os
import sys

archivo = "usuarios.txt"
# Creamos una lista para almacenar los valores
usuarios = []

# Comprobamos que el fichero exista, sino, lo creamos
if not os.path.exists(archivo):
    with open(archivo, "w"):
        # Creamos el fichero
        pass

# Pedimos los 3 usuarios por input()
for i in range(3):
    nombre = input(f"Nombre {i+1}: ")

    # Implementamos control de errores
    try:
        edad = int(input(f"Edad {i+1}: "))

        # Comprobamos que sea una edad real
        if not 0 < edad <= 120:
            raise ValueError

    # Capturamos el error lanzado si no introducimos un dato correcto (ValueError)
    except ValueError:
        print("\nIntroduce una edad correcta")
        sys.exit()

    # Creamos un diccionario para el nuevo usuario
    usuario = {"nombre":nombre, "edad":edad}
    # Añadimos este nuevo usuario a la lista global
    usuarios.append(usuario)

print(usuarios)
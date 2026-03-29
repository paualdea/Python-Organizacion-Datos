# Programación en Python: Organización de datos

Este proyecto ha sido desarrollado como parte de la **Actividad de evaluación 2** de la Unidad de Trabajo 4 (UT4): "Entrada y salida de información".

El programa implementa un sistema que pide información (nombre y edad) de 3 usuarios, los ordena en una lista de diccionarios y los añade a un fichero de texto (`usuarios.txt`) También se valida la entrada de datos y gestionan excepciones para el excelente funcionamiento de la aplicación.

## Características Principales

* **Validación**: Implementación de estrcturas de control `try-except` para capturar errores de tipo (`ValueError`) cuando el usuario introduce un valor erróneo o un edad incorrecta.
* **Uso de Listas y Diccionarios**: Se implementa el uso de listas y diccionarios para organizar los datos recogidos.
* **Gestión de Archivos**: Uso de la sentencia `with open()` para asegurar la apertura y cierre automático de los archivos.
* **Codificación UTF**: Uso de `encoding="utf-8"` para permitir el uso de carácteres especiales.

## Funcionamiento

El programa sigue el siguiente flujo:

1. **Inicialización**: Se comprueba la existencia del archivo `usuarios.txt` y lo crea si es necesario.
2. **Entrada de datos**: Se ejecuta un bucle `for` 3 veces para pedir el nombre y edad del usuario. Se almacenan los resultados de este bucle en la lista `usuarios`.
3. **Escritura y Organización**:
    * Accedemos al fichero en modo *write* (`w`).
    * Recorriendo la lista `usuarios`, formateamos cada línea (`nombre - edad`) y la escribimos en `usuarios.txt`.

## Instrucciones de Uso

Para ejecutar este programa, es necesario descargar el [código fuente](https://git.paualdea.com/paualdea/Python-Organizacion-Datos/-/releases) y ejecutar el fichero `organizacion_datos.py`.

---
Este proyecto sirve como evidencia del aprendizaje sobre el manejo de archivos en Python, de la asignatura **Programación en Python**.
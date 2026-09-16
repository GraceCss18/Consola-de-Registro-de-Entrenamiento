# *Registro de Entrenamiento (GYM) *
Consola en python para registrar los ejercicio de un usuario en el gimnasio, ver el historial, calcular el progeso, buscar ejercicios y filtrar por peso levantado.

## ¿Cómo ejecutarlo?

python3 main.py

Al iniciar la consola, muestra un mensaje de bievenida una sola ve y después entra en un menú que se repite hasta que eliges "Salir".

## Menú principal

1. Agregar el ejercicio del día
2. Ver historial semanal
3. Calcular progreso
4. Buscar ejercicio
5. Filtrar por peso mínimo 
6. Salir

## ¿Cómo guarda la información?

### Historial: 
Una lusta que empieza vacía, cada ejericico que se agrega se guarda ahí como un diccionarios con las siguientes etiquetas: *dia*, *nombre*, *series*, *repeteciones*, *peso*.

### ejerciciosDisponibles:
Un diccionario que agrupa los ejercicios por grupo muscular (*pecho*, *espalda*, *piernas*, *hombros*, *brazos*, *core*, *cardio*), cada uno con una lista de nombres de ejercicios.
Al agregar un ejercicio, se elige de esta lista (no se escribe libremente), para evitar errores de tipeo.

### grupos:
Una lista con los nombrs de los grupos muscualres, en el mismo orden que las etiquetas de *ejerciciosDisponibles*

Nada de est se guarda en un archivo, si cierras el programa, el historial se pierde y empieza vació la próxima vez.

## Funciones del programa 

### Función               | Qué hace
--------------------------|---------------------
mostrarBievenida()        | Muestra el mensaje de bienvenida, una sola vez al inciiar
elegirEjercicio()         | Primero pregunta el grupo muscular, luego el ejercicio específico de ese grupo y devuelve el nombre elegido.
mostrarMenu()             | Muestra las 6 opciones del menú.
ejercicioYaRegistrado()   | Revisa si ya existe un registro con ese mismo día y nombre, devuelve *True* o *False*.
#git add: para agregar los archivos que estan untracked en el respositorio
#git unit para crear un nuevo repositorio 
#git status para ver los repositorios
#git restore es para eliminar los cambios que haya realizado en un archivo
#con git add . se guardan todo lo que se agrego en todos los archivos
#git commit -m "texto"
#git log --oneline

# CONSOLA DE : REGISTRO DE ENTRENAMIENTO (GYM)
#DEBE MOSTRAR:
# Agregar ejercicio del día, ver historial semanal, 
# calcular progreso, buscar ejercicio, salir

#creare primero una caja para guardar el registro de entrenamiento
Historial = []

#creo el def de mostrar bienvenida
def mostrarBievenida():
    print("========================================")
    print("BIEVENIDO A SU REGISTRO DE ENTRENAMIENTO")
    print("========================================")

mostrarBievenida()


#haré un diccionario de ejericicos para que el usuario escoja y no agregue ejercicios inventados (no aún)
ejerciciosDisponibles = {
"Pecho" : ["Press de banca plano", "Press icnlinado con mancueras", "Aperturas en polea alta", "Fondos en paralelas", "Flexiones de pecho (Push-ups)" ],
"Espalda" : ["Dominadas pronadas", "Jalón al pecho con agarre ancho", "Remo con barra", "Remo unilateral con mancuerna", "Peso muerto convecional"],
"Piernas" : ["Sentadilla trasera con barra", "Prensa inclinada 45°", "Peso muerto rumano", "Extendiones de cuádriceps", "Curl femoral sentado", "Zancadas / Sentadilla búlgaras", "Elevación de talones"],
"Hombros" : ["Press militar sentado", "Elevaciones laterales", "Face pull", "Elevaciones frontales"],
"Brazos" : ["Curl de bíceps con barra Z", "Curl martillo", "Extensiones de tríceps en polea", "Press francés"],
"Core" : ["Plancga abdominal isométrica", "Elevanción de piernas colgado", "Crunch en polea"],
"Cardio" : ["Caminadora", "Spinning", "Eliptica", "Remo ergométrico", "Escaladora", "Salto con cuerda", "Burpees", "Jumping Jacks", "Mountin Climbers", "Sprints en pista", "Sombras de boxeo", "Sled Push"]
}

#voy a mostrar ahora los grupos que he creado
grupos = ["Pecho", "Espalda", "Piernas", "Hombros", "Brazos", "Core", "Cardio"]


def elegirEjercicio():
    print("\nGrupos musculares disponibles:")
    for i, grupo in enumerate(grupos, start=1):
        print(f"{i}. {grupo}")

    opcion = int(input("Elige el número del grupo muscular: "))
    grupoElegido = grupos[opcion - 1]
    ejercicioDelGrupo = ejerciciosDisponibles[grupoElegido]

    print(f"\nEjercicios de {grupoElegido}:")
    for i, nombre in enumerate(ejercicioDelGrupo, start=1):
        print(f"{i}. {nombre}")

    opcion = int(input("Elige el número del ejercicio: "))
    return ejercicioDelGrupo[opcion - 1]
    

def mostrarMenu():
    #mostrare las ocpiones que el usuario puede escoger 

    print("\n=== REGISTRO DE ENTRENAMIENTO ===")
    print("1. Agregar el ejercicio del día")
    print("2. Ver histroial semanal")
    print("3. Calcular progreso")
    print("4. Buscar ejercicio")
    print("5. Filtrar por peso mínimo")
    print("6. Salir")


def ejercicioYaRegistrado(dia, nombre):
    #se revisa si ya existe un registro con ese mismo día 
    #y el mismo ejercicios dentro del historial. Devuelve un true o false

    for ejercicio in Historial:
        if ejercicio["dia"] == dia and ejercicio["nombre"] == nombre:
            return True
    return False


def agregarEjercicio():
    #pide los datos de un ejercicio y los guardara en el historial
    print("\n--- Agregar ejercicio----")
    dia = input("¿Qué día fue? (ej: lunes): ").lower()

    #como ya esta el registeo de los ejercicios disponibles,
    #solo debe escoger lo que se encuentre disponible
    nombre = elegirEjercicio()

    #avisa si ese ejercicio ya se había registrado ese mismo día
    #pero se deja seguir agregandolo de todas formas
    if ejercicioYaRegistrado(dia, nombre):
        print(f"Ya tenías registrado '{nombre}' el {dia}. lo agregamos igual como una serie más")

    series = int(input("¿Cuántas series hiciste?: "))
    repeteciones = int(input("¿Cuántas repretciones por serie?: "))

    peso = float(input("¿Con cuánto peso? (en kilos): "))

    ejercicio = {
        "dia": dia, 
        "nombre": nombre,
        "series": series, 
        "repeticiones": repeteciones,
        "peso": peso, 
    }

    #guarda la informacion que se registra en nombre y dia
    Historial.append(ejercicio)
    print(f"¡Listo! Se guardó '{nombre}' del {dia}")


def verHistorial():
    #se muestra todos los ejericicios guardados en orden
    print("\n----Historial semanal----")

    #utilizo len para poder ver cuantas fichas tengo dentro 
    #de mi lista historial
    if len(Historial) == 0:
        print("Todavía no hay ejericicos guardados")
        return

    #recorremos la lista ficha por ficha creada en el anterior def 
    #y mostrarmos los datos
    for i, ejercicio in enumerate(Historial, start=1):
        print(
            f"{i}. [{ejercicio['dia']}] {ejercicio['nombre']} "
            f"{ejercicio['series']} series x {ejercicio['repeticiones']} reps "
            f"con {ejercicio['peso']} kg"
        )

def promedioPeso(registros):
    #calcula el peso promedio de una lista de registrol del historial
    #usando sum() y len(), igual que en el ejercicio de promedio

    pesos = []
    for registro in registros:
        pesos.append(registro["peso"])

    suma = sum(pesos)
    cantidad = len(pesos)
    return suma / cantidad


def calcularProgeso():
    #compara el primer y el último regsitro de un mismo ejercicio
    #para ver si el peso levantando subió, bajó o quedó igual y muestra 
    #también el peso promedio de todos esos registros

    print("\n----Calcular progeso---------")
    nombre = input("¿De qué ejercicio quieres ver tu progeso").lower()

    #se busca dentro del historial los ejercicios que tengan ese nombre

    registros = [e for e in Historial if e["nombre"] == nombre]

    if len(registros) == 0:
        print("No enconté ese ejercico en tu historial.")
        return

    promedio = promedioPeso(registros)
    print(f"Peso primedio en '{nombre}': {promedio} kg")

    if len(registros) ==1:
        print("Solo tienes un registro de ese ejercicios, todavía no hay progreso que comparar.")
        return

    primero = registros[0]
    ultimo = registros[-1]
    diferencia = ultimo["peso"] - primero["peso"]

    print(f"Primer registro: {primero['peso']} kg ({primero['dia']})")
    print(f"Ultimo registro: {ultimo['peso']} kg ({ultimo['dia']})")

    if diferencia >0:
        print(f"¡Vas mejorando! Subiste {diferencia} kg ({primero['dia']})") 
    elif diferencia < 0:
        print(f"Bajaste {abs(diferencia)} kg en '{nombre}'. ¡Tranquila baby, eso también pasa!")
    else:
        print(f"Te mantuviste igual en '{nombre}'")

def buscarEjercicio():
    #Busca el ejercicio por nombre y muestra todos los que coinciden
    print("\n--------Buscar ejercicio-------")
    nombre = input("¿Qué ejercicio buscas?: ").lower()

    encontrados = [e for e in Historial if nombre in e["nombre"]]

    if len(encontrados) == 0:
        print("No encontré ningún ejercico con ese nombre")
        return

    for ejercicio in encontrados:
        print(
            f"[{ejercicio['dia']}] {ejercicio['nombre']} -"
            f"{ejercicio['series']} series x {ejercicio['repeticiones']} reps"
            f"con {ejercicio['peso']} kg"
        )


def filtrarPorPeso(pesoMinimo=50):
    #devuelve una lista con los ejercicios cuyo peso fue mayor a 
    #pesoMinimo, sino le das ese dato, usa 50kg por defecto

    resultado = []
    for ejercicio in Historial:
        if ejercicio["peso"] > pesoMinimo:
            resultado.append(ejercicio)
    return resultado

def mostrarFiltradoPorPeso():
    #pregunta un peso mínimo y muestra los ejercicios que los supera
    print("\n---Filtrar por peso mínimo---")
    texto = input("¿Peso mínimo en kg? (déjalo vacío para usar 50kg por defecto): ")

    if texto == "":
        #el usuario no escrbió nada: utiliza el filtrarPorPeso con el valor de defecto
        encontrados = filtrarPorPeso()
    else:
        encontrados = filtrarPorPeso(float(texto))

    if len(encontrados) == 0:
        print("No hay ejercicios que superen ese peso.")
        return

    for ejercicio in encontrados:
        print(
            f"[{ejercicio['dia']} {ejercicio['nombre']}] - "
            f"{ejercicio['series']} series x {ejercicio['repeticiones']} reps"
            f"con {ejercicio['peso']} kf"
        )
    
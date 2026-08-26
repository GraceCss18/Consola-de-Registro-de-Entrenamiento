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

def mostrarMenu():
    print("REGISTRE SU ENTRENAMIENTO DEL DÍA ")
    print("")
    print("")
    print("")

#haré un diccionario de ejericicos para que el usuario escoja y no agregue ejercicios inventados (no aún)
ejerciciosDisponibles = {
"Pecho " : ["Press de banca plano", "Press icnlinado con mancueras", "Aperturas en polea alta", "Fondos en paralelas", "Flexiones de pecho (Push-ups)" ],
"Espalda" : ["Dominadas pronadas", "Jalón al pecho con agarre ancho", "Remo con barra", "Remo unilateral con mancuerna", "Peso muerto convecional"],
"Piernas" : ["Sentadilla trasera con barra", "Prensa inclinada 45°", "Peso muerto rumano", "Extendiones de cuádriceps", "Curl femoral sentado", "Zancadas / Sentadilla búlgaras", "Elevación de talones"],
"Hombros" : ["Press militar sentado", "Elevaciones laterales", "Face pull", "Elevaciones frontales"],
"Brazos" : ["Curl de bíceps con barra Z", "Curl martillo", "Extensiones de tríceps en polea", "Press francés"],
"Core" : ["Plancga abdominal isométrica", "Elevanción de piernas colgado", "Crunch en polea"],
"Cardio" : ["Caminadora", "Spinning", "Eliptica", "Remo ergométrico", "Escaladora", "Salto con cuerda", "Burpees", "Jumping Jacks", "Mountin Climbers", "Sprints en pista", "Sombras de boxeo", "Sled Push"]
}

#voy a mostrar ahora los grupos que he creado
grupos = ["Pecho", "Espalda", "Piernas", "Hombres", "Brazos", "Core", "Cardio"]

#ahora creare el def para pedirle al usuario elegir el ejercicio de los que se agrego
#necesito que me muestre primero el grupo muscular y luego los ejericicos de ese grupo 

#le mostrare la opción de los grupos musculares
print ("\nGrupos musculares disponibles:")

#ahora usuare for para mostrarle al usuario los grupos musculares y la lista dentro de ese grupo muscular
#para que pueda escojer
#escogí la opcion de i y enumerate para que me los enumere como opciones para el usuario 

for i, grupo in enumerate(grupos, start=1):
    print(f"{i}. {grupo}")

opcionTexto = input("Elige el número del grupo muscular: ")


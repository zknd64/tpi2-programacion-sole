import random

def jugar():
    nombre = input("Ingrese su nombre: ")
    puntaje = 0

    frutas = {"Manzana": 10,"Pera": 5,"Uva": 8, "Banana": 4, "kiwi": 2}

    nombres_frutas = list(frutas.keys())

    for ronda in range(1, 6):

        fruta1 = random.choice(nombres_frutas)
        fruta2 = random.choice(nombres_frutas)
        fruta3 = random.choice(nombres_frutas)
        fruta4 = random.choice(nombres_frutas)
        fruta5 = random.choice(nombres_frutas)
        

        resultado = (
            frutas[fruta1]
            + frutas[fruta2]
            + frutas[fruta3]
            + frutas[fruta4]
            + frutas[fruta5]
        )

        print("\nRonda", ronda)
        print(fruta1, "+", fruta2, "+", fruta3, "+", fruta4, "+", fruta5, "= ?")

        respuesta = int(input("Ingrese el resultado: "))

        if respuesta == resultado:
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto.")
            print("La respuesta correcta era:", resultado)

    print("\nJuego terminado.")
    print("Puntaje obtenido:", puntaje)

    guardar_puntaje(nombre, puntaje)

def guardar_puntaje(nombre, puntaje):
    archivo = open("puntajes.txt", "a")
    archivo.write(nombre + ";" + str(puntaje) + "\n")
    archivo.close()
def mostrar_ranking():
    try:
        archivo = open("puntajes.txt", "r")

        print("\n=== RANKING ===")

        for linea in archivo:
            datos = linea.strip().split(";")
            nombre = datos[0]
            puntos = int(datos[1])

            print(nombre, "-", puntos, "puntos")

        archivo.close()

    except FileNotFoundError:
        print("No hay puntajes guardados todavía.")

def mostrar_menu():
    opcion = 0

    while opcion != 3:

        print("\n=== JUEGO DE FRUTAS ===")
        print("1. Jugar")
        print("2. Ver ranking")
        print("3. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            jugar()

        elif opcion == 2:
            mostrar_ranking()

        elif opcion == 3:
            print("Gracias por jugar.")

        else:
            print("Opción inválida.")
# Programa principal
mostrar_menu()
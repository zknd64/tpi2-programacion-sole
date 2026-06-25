import random
def adivinar_resultado():
    nombre = input("Ingrese su nombre y apellido: ")
    puntaje = 0

    frutas = {"Manzana": 10,"Pera": 5,"Uva": 8, "Banana": 4, "kiwi": 2}

    nombres_frutas = list(frutas.keys())

    for ronda in range(1, 6):

        fruta1 = random.choice(nombres_frutas)
        fruta2 = random.choice(nombres_frutas)
        fruta3 = random.choice(nombres_frutas)
        fruta4 = random.choice(nombres_frutas)
        fruta5 = random.choice(nombres_frutas)
        

        frutas_sorteadas = [fruta1, fruta2, fruta3, fruta4, fruta5]

        resultado = 0

        for fruta in frutas_sorteadas:
            resultado += frutas[fruta]

        print("\nRonda", ronda)
        print(fruta1, "+", fruta2, "+", fruta3, "+", fruta4, "+", fruta5, "= ?")

        respuesta = int(input("Ingrese el resultado: "))

        if respuesta == resultado:
            print("Resultado excelente ")
            puntaje += 1
        else:
            print("Resultado incorrecto")
            print("La respuesta correcta era:", resultado)

    print("\nJuego terminado.")
    print("Puntaje obtenido:", puntaje)

    guardar_puntaje_frutas(nombre, puntaje)

def guardar_puntaje_frutas(nombre, puntaje):
    archivo = open("puntajes.txt", "a")
    archivo.write(nombre + ";" + str(puntaje) + "\n")
    archivo.close()

def mostrar_ranking_frutas():
    try:
        archivo = open("puntajes.txt", "r")

        print("\n=== RANKING FRUTAS ===")

        for linea in archivo:
            datos = linea.strip().split(";")
            nombre = datos[0]
            puntos = int(datos[1])

            print(nombre, "-", puntos, "puntos")

        archivo.close()

    except FileNotFoundError:
        print("No se han guardado puntajes aun.")

def mostrar_menu_juego_frutas():
    opcion = 0

    while opcion != 3:

        print("\n🍇🍌🍎🍊 BIENVENIDO AL JUEGO DE FRUTAS 🍇🍌🍎🍊")
        print("1. Jugar juego🕹️")
        print("2. mostrar ranking🥇")
        print("3. Volver al Menú Principal 🔙")

        opcion = int(input("Seleccione la opcion que desee: "))

        if opcion == 1:
            adivinar_resultado()

        elif opcion == 2:
            mostrar_ranking_frutas()

        elif opcion == 3:
            print("Saliendo del juego de frutas...")
        else:
            print("Opción no valida ❌.")
mostrar_menu_juego_frutas()
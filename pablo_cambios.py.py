def guardar_puntaje(nombre, puntos):
    with open("ranking_secuencia.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntos}\n")


def mostrar_ranking():
    print("\n🏆 --- RANKING DE JUGADORES --- 🏆")

    if not os.path.exists("ranking_secuencia.txt"):
        print("Todavía no hay partidas registradas.")
        return

    jugadores = []

    with open("ranking_secuencia.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea or "," not in linea:
                continue

            datos = linea.split(",")
            nombre = datos[0]
            puntos = int(datos[1])
            jugadores.append((nombre, puntos))

    if not jugadores:
        print("Todavía no hay partidas registradas.")
        return

    jugadores.sort(key=lambda jugador: jugador[1], reverse=True)

    for puesto, (nombre, puntos) in enumerate(jugadores, start=1):
        print(f"{puesto} - {nombre} - {puntos} puntos")


# ------------------ JUEGO ------------------

def jugar_secuencia():
    print("\n===== COMPLETA LA SECUENCIA =====")
    nombre = input("Ingrese su nombre: ")

    if nombre.strip() == "":
        nombre = "Anónimo"

    puntos = 0

    for ronda in range(1, 4):
        secuencia = [2, 4, 6, 8]
        posicion_oculta = random.randint(0, 3)
        correcta = secuencia[posicion_oculta]

        visible = []
        for numero in secuencia:
            visible.append(str(numero))

        visible[posicion_oculta] = "?"

        print("\nRonda", ronda)
        print(" - ".join(visible))

        try:
            respuesta = int(input("¿Qué número falta?: "))
            if respuesta == correcta:
                print("¡Correcto!")
                puntos += 10
            else:
                print("Incorrecto.")
                print("La respuesta era:", correcta)
        except ValueError:
            print("Debe ingresar un número válido. Perdiste esta ronda.")

    print("\nJuego terminado.")
    print("Puntaje:", puntos)

    guardar_puntaje(nombre, puntos)


# ------------------ MENÚ DEL JUEGO (SUBMENÚ) ------------------

def menu_secuencia():
    while True:
        print("\n===== COMPLETA LA SECUENCIA =====")
        print("1. Jugar")
        print("2. Ver ranking")
        print("3. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número.")
            continue

        if opcion == 1:
            jugar_secuencia()

        elif opcion == 2:
            mostrar_ranking()

        elif opcion == 3:
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción inválida.")
            
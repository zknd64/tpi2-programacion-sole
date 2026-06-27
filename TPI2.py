import random
import os

# JUEGO 1: EL JUEGO DE FRUTAS

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


# JUEGO 2: COMPLETA LA SECUENCIA

def guardar_puntaje_secuencia(nombre, puntos):
    """Guarda el nombre y puntaje al final del archivo."""
    with open("ranking.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntos}\n")

def mostrar_ranking_secuencia():
    """Lee el archivo, ordena los puntajes de mayor a menor y los muestra."""
    print("\n🏆 --- RANKING DE JUGADORES (SECUENCIA) --- 🏆")
    
    if not os.path.exists("ranking.txt"):
        print("Aún no hay partidas registradas. ¡Sé el primero!")
        return

    lista_jugadores = []
    
    with open("ranking.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                nombre = partes[0]
                puntos = int(partes[1])
                lista_jugadores.append((nombre, puntos))
    
    lista_jugadores.sort(key=lambda jugador: jugador[1], reverse=True)
    
    for puesto, (nombre, puntos) in enumerate(lista_jugadores, start=1):
        print(f"{puesto}. {nombre} -> {puntos} pts")
    print("---------------------------------")

def jugar_secuencia():
    print("\n--- JUEGO: COMPLETA LA SECUENCIA ---")
    nombre = input("Ingresá tu nombre: ").strip()
    if not nombre:
        nombre = "Anónimo"
        
    puntos = 0
    
    for ronda in range(3):
        secuencia = [2, 4, 6, 8] 
        posicion_oculta = random.randint(0, 3)
        correcta = secuencia[posicion_oculta]
        
        visible = [str(n) for n in secuencia]
        visible[posicion_oculta] = "?"
        print(f"\nRonda {ronda+1}/3 - Secuencia: {' - '.join(visible)}")
        
        try:
            intento = int(input("¿Qué número falta?: "))
            if intento == correcta:
                print("¡Acertaste! 🎉 +10 puntos.")
                puntos += 10
            else:
                print(f"Incorrecto 😢. Era {correcta}.")
        except ValueError:
            print("Error: No ingresaste un número. Pasamos a la siguiente ronda.")
            
    print(f"\n¡Juego terminado! Conseguiste: {puntos} puntos.")
    guardar_puntaje_secuencia(nombre, puntos)

def mostrar_menu_secuencia():
    while True:
        print("\n=== MENÚ SECUENCIA ===")
        print("1. Jugar 'Completa la Secuencia'")
        print("2. Ver Ranking de Jugadores (Archivo)")
        print("3. Volver al Menú Principal 🔙")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            jugar_secuencia()
        elif opcion == "2":
            mostrar_ranking_secuencia()
        elif opcion == "3":
            print("Saliendo del juego de Secuencias...")
            break
        else:
            print("Opción inválida. Por favor, elegí 1, 2 o 3.")


# JUEGO 3: AVENTURA DE MULTIPLICACIONES

def guardar_puntaje_multiplicar(archivo_ranking: str, nombre: str, puntaje: int) -> None:
    """Registra de manera persistente el nombre y puntaje en el archivo."""
    try:
        with open(archivo_ranking, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{puntaje}\n")
    except IOError:
        print("Error: No se pudo guardar el puntaje en el archivo.")

def mostrar_ranking_multiplicar(archivo_ranking: str) -> None:
    """Lee el archivo, ordena los puntajes de mayor a menor y los muestra."""
    print("\n--- 🏆 TABLA DE PUNTAJES (RANKING) 🏆 ---")
    if not os.path.exists(archivo_ranking):
        print("Aún no hay puntajes registrados. ¡Sé el primero!")
        return

    lista_ranking = []
    try:
        with open(archivo_ranking, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    nombre, puntaje_str = linea.split(",")
                    lista_ranking.append((nombre, int(puntaje_str)))
        
        lista_ranking.sort(key=lambda x: x[1], reverse=True)
        
        for puesto, (nombre, puntaje) in enumerate(lista_ranking[:5], start=1):
            print(f"{puesto}. {nombre}: {puntaje} puntos")
    except (IOError, ValueError):
        print("Error al leer el archivo de ranking.")

def solicitar_entero(mensaje: str) -> int:
    """Valida la entrada del usuario de forma robusta ante errores de tipo."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Entrada inválida. Por favor, escribe un número entero.")

def seccion_juego(archivo_ranking: str) -> None:
    """Ciclo repetitivo de 5 preguntas de multiplicación aleatorias."""
    print("\n--- 🎮 ¡A JUGAR Y MULTIPLICAR! 🎮 ---")
    nombre = input("Escribe tu nombre: ").strip()
    if not nombre:
        nombre = "Jugador Anónimo"

    puntaje_total = 0
    total_preguntas = 5

    for i in range(1, total_preguntas + 1):
        num1 = random.randint(2, 10)
        num2 = random.randint(2, 10)
        resultado_correcto = num1 * num2

        print(f"\nPregunta {i}/{total_preguntas}: ¿Cuánto es {num1} x {num2}?")
        respuesta_usuario = solicitar_entero("Tu respuesta: ")

        if respuesta_usuario == resultado_correcto:
            print("🌟 ¡Excelente! Respuesta correcta. (+20 puntos)")
            puntaje_total += 20
        else:
            print(f"😢 ¡Casi! El resultado correcto era {resultado_correcto}.")

    print(f"\n🎉 ¡Terminaste, {nombre}! Tu puntaje final es: {puntaje_total} puntos.")
    guardar_puntaje_multiplicar(archivo_ranking, nombre, puntaje_total)

def seccion_aprender_tablas() -> None:
    """Muestra de forma secuencial y repetitiva la tabla que el niño elija."""
    print("\n--- 📖 APRENDE LAS TABLAS DE MULTIPLICAR 📖 ---")
    print("¿Qué tabla te gustaría repasar? (Ingresa un número del 1 al 10)")
    tabla = solicitar_entero("Tabla del: ")
    
    print(f"\n--- Tabla del {tabla} ---")
    for i in range(1, 11):
        print(f"👉 {tabla} x {i} = {tabla * i}")
    input("\nPresiona Enter para volver al menú...")

def seccion_calculo_mental() -> None:
    """Estructura de datos: Diccionario para enseñar trucos de cálculo mental."""
    trucos = {
        2: "Multiplicar por 2 es simplemente buscar el DOBLE del número. (Ej: 2 x 6 es 6 + 6 = 12).",
        5: "Los resultados de la tabla del 5 siempre terminan en 0 o en 5. ¡Prueba saltando de 5 en 5!",
        9: "¡El truco de las manos! Si multiplicas 9 x 3, dobla tu tercer dedo. A la izquierda te quedan 2 y a la derecha 7: ¡27!",
        10: "Para multiplicar por 10, solo escribe el mismo número y agrégale un CERO al final. (Ej: 10 x 4 = 40)."
    }

    print("\n--- 🧠 TRUCOS DE CÁLULCO MENTAL 🧠 ---")
    print("Elige un número para aprender su secreto de cálculo rápido: (2, 5, 9, 10)")
    opcion = solicitar_entero("Tu opción: ")

    if opcion in trucos:
        print(f"\n💡 Secreto del {opcion}: {trucos[opcion]}")
    else:
        print("\nPronto añadiremos más trucos para ese número. ¡Sigue practicando!")
    input("\nPresiona Enter para volver al menú...")

def mostrar_menu_multiplicar():
    """Controla el flujo principal del software educativo."""
    ARCHIVO_DATOS = "ranking_multiplicar.txt"
    
    while True:
        print("\n======================================")
        print("    🎈 AVENTURA DE MULTIPLICACIONES 🎈  ")
        print("======================================")
        print("1. 🎮 Jugar (Desafío Aleatorio)")
        print("2. 📖 Estudiar las Tablas")
        print("3. 🧠 Trucos de Cálculo Mental")
        print("4. 🏆 Ver Tabla de Puntajes")
        print("5. 🚪 Volver al Menú Principal 🔙")
        print("======================================")
        
        opcion = solicitar_entero("Selecciona una opción (1-5): ")

        if opcion == 1:
            seccion_juego(ARCHIVO_DATOS)
        elif opcion == 2:
            seccion_aprender_tablas()
        elif opcion == 3:
            seccion_calculo_mental()
        elif opcion == 4:
            mostrar_ranking_multiplicar(ARCHIVO_DATOS)
        elif opcion == 5:
            print("\nSaliendo del juego de Multiplicaciones...")
            break
        else:
            print("❌ Opción inválida. Elige un número del 1 al 5.")


# JUEGO 4: PALABRA OCULTA

palabras = {
    "Animales": [
        ("leon", "Es el rey de la selva"),
        ("jirafa", "Tiene el cuello largo"),
        ("elefante", "Tiene trompa"),
        ("tigre", "Felino de rayas"),
        ("conejo", "Tiene orejas largas")
    ],
    "Provincias": [
        ("cordoba", "Provincia mediterranea"),
        ("mendoza", "Famosa por el vino"),
        ("salta", "La linda"),
        ("buenosaires", "Capital del pais"),
        ("jujuy", "Paisajes coloridos")
    ],
    "Profesiones": [
        ("medico", "Trabaja en hospitales"),
        ("docente", "Enseña en la escuela"),
        ("ingeniero", "Diseña soluciones"),
        ("abogado", "Trabaja en leyes"),
        ("cocinero", "Prepara comida")
    ]
}

def mostrar_palabra(palabra, letras):
    resultado = ""
    for i in range(len(palabra)):
        letra = palabra[i]
        if letra in letras:
            resultado = resultado + letra + " "
        else:
            resultado = resultado + "_ "
    return resultado

def gano(palabra, letras):
    for i in range(len(palabra)):
        if palabra[i] not in letras:
            return False
    return True

def guardar_puntaje_oculta(nombre, puntos):
    # Se modificó el archivo a 'puntajes_oculta.txt' para no pisar el Juego 1
    archivo = open("puntajes_oculta.txt", "a")
    archivo.write(nombre + ";" + str(puntos) + "\n")
    archivo.close()

def ordenar_seleccion(lista):
    for i in range(len(lista) - 1):
        posicion_mayor = i
        for j in range(i + 1, len(lista)):
            if lista[j][1] > lista[posicion_mayor][1]:
                posicion_mayor = j
        aux = lista[i]
        lista[i] = lista[posicion_mayor]
        lista[posicion_mayor] = aux
    return lista

def mostrar_ranking_oculta():
    try:
        archivo = open("puntajes_oculta.txt", "r")
        ranking = []
        for linea in archivo:
            datos = linea.strip().split(";")
            nombre = datos[0]
            puntos = int(datos[1])
            ranking.append([nombre, puntos])
        archivo.close()
        ranking = ordenar_seleccion(ranking)
        print("\nRANKING:")
        for i in range(len(ranking)):
            print(ranking[i][0], "-", ranking[i][1])
    except:
        print("No hay ranking aun.")

def jugar_oculta():
    print("\nCATEGORIAS:")
    print("1 - Animales")
    print("2 - Provincias")
    print("3 - Profesiones")

    opcion = input("Elegir categoria: ")

    if opcion == "1":
        categoria = "Animales"
    elif opcion == "2":
        categoria = "Provincias"
    elif opcion == "3":
        categoria = "Profesiones"
    else:
        print("Opcion invalida")
        return

    lista_palabras = palabras[categoria]
    indice = random.randint(0, len(lista_palabras) - 1)
    palabra = lista_palabras[indice][0]
    pista = lista_palabras[indice][1]
    letras = []
    intentos = 6

    print("\nPISTA:", pista)

    while intentos > 0 and not gano(palabra, letras):
        print("\nPalabra:", mostrar_palabra(palabra, letras))
        print("Intentos:", intentos)
        print("1 - Ingresar letra")
        print("2 - Adivinar palabra")

        opcion = input("Opcion: ")

        if opcion == "1":
            letra = input("Letra: ")
            if letra not in letras:
                letras.append(letra)
                if letra not in palabra:
                    intentos = intentos - 1
            else:
                print("Ya ingresada")
        elif opcion == "2":
            intento = input("Palabra: ")
            if intento == palabra:
                letras = []
                for i in range(len(palabra)):
                    letras.append(palabra[i])
            else:
                print("Incorrecto")
                intentos = intentos - 1
        else:
            print("Opcion invalida")

    if gano(palabra, letras):
        print("\nGANASTE")
        puntos = intentos * 10
        print("Puntos:", puntos)
        nombre = input("Nombre: ")
        guardar_puntaje_oculta(nombre, puntos)
    else:
        print("\nPERDISTE. La palabra era:", palabra)

def menu_oculta():
    opcion = ""
    while opcion != "0":
        print("\n===================")
        print("PALABRA OCULTA")
        print("===================")
        print("1 - Jugar")
        print("2 - Ranking")
        print("0 - Volver al Menú Principal 🔙")

        opcion = input("Opcion: ")

        if opcion == "1":
            jugar_oculta()
        elif opcion == "2":
            mostrar_ranking_oculta()
        elif opcion == "0":
            print("Saliendo del juego Palabra Oculta...")
        else:
            print("Invalido")


# PROGRAMA PRINCIPAL: MENÚ GENERAL DEL PROYECTO

def menu_general():
    opcion_general = 0

    while opcion_general != 5:
        print("\n=========================================")
        print("🎮 MULTIJUEGOS - PROYECTO GRUPAL 🎮")
        print("=========================================")
        print("1. Jugar al Juego de adivinar frutas 🍎")
        print("2. Jugar al Juego de Secuencias 🔢")
        print("3. Jugar al Juego de Multiplicaciones 🎈")
        print("4. Jugar al Juego de Palabra Oculta 🔤")
        print("5. Salir del Programa Completo ❌")
        print("=========================================")
        
        try:
            opcion_general = int(input("Seleccione qué juego quiere iniciar: "))

            if opcion_general == 1:
                mostrar_menu_juego_frutas()  
            elif opcion_general == 2:
                mostrar_menu_secuencia()  
            elif opcion_general == 3:
                mostrar_menu_multiplicar()  
            elif opcion_general == 4:
                menu_oculta()  
            elif opcion_general == 5:
                print("\n¡Gracias por jugar a nuestro proyecto grupal! ¡Hasta luego! 👋")
            else:
                print("Opción no válida en el Menú General ❌.")
        except ValueError:
            print("Por favor, ingresa un número válido de opción ❌.")

# Arranca todo el programa integrado con los 4 juegos
menu_general()
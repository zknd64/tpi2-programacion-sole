import random
import os

# --- FUNCIONES DE PERSISTENCIA (ARCHIVOS) ---

def guardar_puntaje(archivo_ranking: str, nombre: str, puntaje: int) -> None:
    """Registra de manera persistente el nombre y puntaje en el archivo."""
    try:
        with open(archivo_ranking, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{puntaje}\n")
    except IOError:
        print("Error: No se pudo guardar el puntaje en el archivo.")

def mostrar_ranking(archivo_ranking: str) -> None:
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
        
        # Ordenamos la lista de tuplas por el segundo elemento (puntaje) de mayor a menor
        lista_ranking.sort(key=lambda x: x[1], reverse=True)
        
        # Mostramos el top 5
        for puesto, (nombre, puntaje) in enumerate(lista_ranking[:5], start=1):
            print(f"{puesto}. {nombre}: {puntaje} puntos")
    except (IOError, ValueError):
        print("Error al leer el archivo de ranking.")

# --- FUNCIONES DE VALIDACIÓN Y CONTROL ---

def solicitar_entero(mensaje: str) -> int:
    """Valida la entrada del usuario de forma robusta ante errores de tipo."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Entrada inválida. Por favor, escribe un número entero.")

# --- LOGICA DEL JUEGO Y ENSEÑANZA ---

def seccion_juego(archivo_ranking: str) -> None:
    """Ciclo repetitivo de 5 preguntas de multiplicación aleatorias."""
    print("\n--- 🎮 ¡A JUGAR Y MULTIPLICAR! 🎮 ---")
    nombre = input("Escribe tu nombre: ").strip()
    if not nombre:
        nombre = "Jugador Anónimo"

    puntaje_total = 0
    total_preguntas = 5

    for i in range(1, total_preguntas + 1):
        # Estructura de datos: Tupla para la multiplicación aleatoria
        num1 = random.randint(2, 10)
        num2 = random.randint(2, 10)
        resultado_correcto = num1 * num2

        print(f"\nPregunta {i}/{total_preguntas}: ¿Cuánto es {num1} x {num2}?")
        respuesta_usuario = solicitar_entero("Tu respuesta: ")

        # Estructura selectiva para verificar la respuesta
        if respuesta_usuario == resultado_correcto:
            print("🌟 ¡Excelente! Respuesta correcta. (+20 puntos)")
            puntaje_total += 20
        else:
            print(f"😢 ¡Casi! El resultado correcto era {resultado_correcto}.")

    print(f"\n🎉 ¡Terminaste, {nombre}! Tu puntaje final es: {puntaje_total} puntos.")
    guardar_puntaje(archivo_ranking, nombre, puntaje_total)

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

# --- MENÚ PRINCIPAL ---

def menu():
    """Controla el flujo principal del software educativo."""
    ARCHIVO_DATOS = "ranking.txt"
    
    while True:
        print("\n======================================")
        print("   🎈 AVENTURA DE MULTIPLICACIONES 🎈  ")
        print("======================================")
        print("1. 🎮 Jugar (Desafío Aleatorio)")
        print("2. 📖 Estudiar las Tablas")
        print("3. 🧠 Trucos de Cálculo Mental")
        print("4. 🏆 Ver Tabla de Puntajes")
        print("5. 🚪 Salir")
        print("======================================")
        
        opcion = solicitar_entero("Selecciona una opción (1-5): ")

        if opcion == 1:
            seccion_juego(ARCHIVO_DATOS)
        elif opcion == 2:
            seccion_aprender_tablas()
        elif opcion == 3:
            seccion_calculo_mental()
        elif opcion == 4:
            mostrar_ranking(ARCHIVO_DATOS)
        elif opcion == 5:
            print("\n👋 ¡Gracias por jugar y aprender! ¡Hasta la próxima!")
            break
        else:
            print("❌ Opción inválida. Elige un número del 1 al 5.")

if __name__ == "__main__":
    menu()





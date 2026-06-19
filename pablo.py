import random
import os

# =====================================================================
# 6. PERSISTENCIA DE INFORMACIÓN (Manejo de Archivo para el Ranking)
# =====================================================================
def guardar_puntaje(nombre, puntos):
    """Guarda el nombre y puntaje al final del archivo."""
    with open("ranking.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntos}\n")

def mostrar_ranking():
    """Lee el archivo, ordena los puntajes de mayor a menor y los muestra."""
    print("\n🏆 --- RANKING DE JUGADORES --- 🏆")
    
    if not os.path.exists("ranking.txt"):
        print("Aún no hay partidas registradas. ¡Sé el primero!")
        return

    lista_jugadores = []
    
    # Leemos el archivo línea por línea
    with open("ranking.txt", "r") as archivo:
        for linea in archivo:
            # Separamos el nombre del puntaje usando la coma
            partes = linea.strip().split(",")
            if len(partes) == 2:
                nombre = partes[0]
                puntos = int(partes[1]) # Lo pasamos a entero para poder ordenarlo
                lista_jugadores.append((nombre, puntos))
    
    # Ordenamos la lista de mayor a menor según los puntos
    lista_jugadores.sort(key=lambda jugador: jugador[1], reverse=True)
    
    # Mostramos el Top en pantalla
    for puesto, (nombre, puntos) in enumerate(lista_jugadores, start=1):
        print(f"{puesto}. {nombre} -> {puntos} pts")
    print("---------------------------------")


# =====================================================================
# 3. MODULARIZACIÓN: Actividad del Juego
# =====================================================================
def jugar_secuencia():
    print("\n--- JUEGO: COMPLETA LA SECUENCIA ---")
    nombre = input("Ingresá tu nombre: ").strip()
    if not nombre:
        nombre = "Anónimo"
        
    puntos = 0
    
    # El juego te hace 3 preguntas seguidas para poder sumar puntos
    for ronda in range(3):
        # 4 y 5. ESTRUCTURA DE DATOS Y CONTROL: Vector (Lista)
        secuencia = [2, 4, 6, 8] 
        posicion_oculta = random.randint(0, 3)
        correcta = ... # El valor oculto se asume según la posición seleccionada
        correcta = secuencia[posicion_oculta]
        
        visible = [str(n) for n in secuencia]
        visible[posicion_oculta] = "?"
        print(f"\nRonda {ronda+1}/3 - Secuencia: {' - '.join(visible)}")
        
        # 7. VALIDACIÓN: Evitamos que se rompa con letras
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
    guardar_puntaje(nombre, puntos) # Guardamos los datos en el archivo TXT


# =====================================================================
# 1. MENÚ PRINCIPAL
# =====================================================================
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar 'Completa la Secuencia'")
        print("2. Ver Ranking de Jugadores (Archivo)")
        print("3. Salir")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            jugar_secuencia()
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("Finalizando el programa. ¡Chau!")
            break
        else:
            print("Opción inválida. Por favor, elegí 1, 2 o 3.")

# Arranca todo el programa
menu()
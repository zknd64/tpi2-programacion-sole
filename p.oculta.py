# JUEGO 4: PALABRA OCULTA
import random

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
        print("PALABRA OCULTA")
        print("1 - Jugar")
        print("2 - Ranking")
        print("0 - Volver al Menú Principal \u25c0\ufe0f")

        opcion = input("Opcion: ")

        if opcion == "1":
            jugar_oculta()
        elif opcion == "2":
            mostrar_ranking_oculta()
        elif opcion == "0":
            print("Saliendo del juego Palabra Oculta...")
        else:
            print("Invalido")

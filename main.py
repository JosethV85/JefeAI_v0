import json
import os


ARCHIVO_MEMORIA = "memoria.json"


def cargar_memoria():

    if not os.path.exists(ARCHIVO_MEMORIA):
        return {}

    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_memoria(memoria):

    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as archivo:
        json.dump(memoria, archivo, indent=4, ensure_ascii=False)


def aprender_nombre(mensaje, memoria):

    mensaje = mensaje.lower()
    palabras = mensaje.split()

    if "me" in palabras and "llamo" in palabras:

        posicion = palabras.index("llamo")

        if posicion + 1 < len(palabras):

            nombre = palabras[posicion + 1]

            nombre = nombre.strip(".,!?")

            nombre = nombre.capitalize()

            memoria["nombre"] = nombre

            guardar_memoria(memoria)

            return f"Mucho gusto, {nombre}. Lo recordaré. 🧠"

    return None


def recordar_nombre(mensaje, memoria):

    mensaje = mensaje.lower()

    preguntas = [
        "cómo me llamo",
        "como me llamo",
        "cual es mi nombre",
        "cuál es mi nombre",
        "dime mi nombre"
    ]

    for pregunta in preguntas:

        if pregunta in mensaje:

            if "nombre" in memoria:

                return f"Te llamas {memoria['nombre']}, jefe 😎"

            else:

                return "Todavía no sé cómo te llamas."

    return None


def analizar_mensaje(mensaje):

    mensaje = mensaje.lower()

    saludos = [
        "hola",
        "buenas",
        "hey",
        "holi",
        "qué tal",
        "que tal",
        "buenos días",
        "buenas tardes",
        "buenas noches"
    ]

    for saludo in saludos:

        if saludo in mensaje:
            return "saludo"

    return "desconocido"


def responder(intencion):

    if intencion == "saludo":
        return "Hola jefe 😎"

    return "Todavía no sé responder eso."


memoria = cargar_memoria()


print("================================")
print("          JEFEAI v0.3")
print("================================")

while True:

    mensaje = input("Tú > ")

    respuesta_nombre = aprender_nombre(mensaje, memoria)

    if respuesta_nombre:
        print("JefeAI >", respuesta_nombre)
        continue

    respuesta_recordar = recordar_nombre(mensaje, memoria)

    if respuesta_recordar:
        print("JefeAI >", respuesta_recordar)
        continue

    if mensaje.lower() == "adios":
        guardar_memoria(memoria)
        print("JefeAI > Nos vemos, jefe.")
        break

    intencion = analizar_mensaje(mensaje)

    respuesta = responder(intencion)

    print("JefeAI >", respuesta)
import json
import os


ARCHIVO_ENTRENAMIENTO = "entrenamiento.json"


def cargar_entrenamiento():

    if not os.path.exists(ARCHIVO_ENTRENAMIENTO):
        return {}

    with open(ARCHIVO_ENTRENAMIENTO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def analizar_mensaje(mensaje, entrenamiento):

    mensaje = mensaje.lower().strip()

    for intencion, ejemplos in entrenamiento.items():

        for ejemplo in ejemplos:

            if ejemplo in mensaje:

                return intencion

    return "desconocido"


def responder(intencion):

    if intencion == "saludo":
        return "Hola jefe 😎"

    if intencion == "despedida":
        return "Nos vemos, jefe."

    return "Todavía no sé responder eso."
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


def consultar_memoria(mensaje, memoria):

    mensaje = mensaje.lower().strip()

    if not mensaje.startswith(("cuál", "cual", "qué", "que", "cómo", "como")):
        return None

    for clave, valor in memoria.items():

        clave_normalizada = clave.lower()

        if clave_normalizada in mensaje:

            return f"Tu {clave} es {valor}, jefe 😎"

    return None
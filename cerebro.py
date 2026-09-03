import json
import os
import unicodedata

ARCHIVO_ENTRENAMIENTO = "entrenamiento.json"
ARCHIVO_RESPUESTAS = "respuestas.json"


def normalizar_texto(texto):
    texto = texto.lower().strip()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto


def cargar_entrenamiento():

    if not os.path.exists(ARCHIVO_ENTRENAMIENTO):
        return {}

    with open(ARCHIVO_ENTRENAMIENTO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def cargar_respuestas():

    if not os.path.exists(ARCHIVO_RESPUESTAS):
        return {}

    with open(ARCHIVO_RESPUESTAS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def analizar_mensaje(mensaje, entrenamiento):

    mensaje = normalizar_texto(mensaje)

    for intencion, ejemplos in entrenamiento.items():

        for ejemplo in ejemplos:

            ejemplo = normalizar_texto(ejemplo)

            if ejemplo in mensaje:
                return intencion

    return "desconocido"


def responder(mensaje, intencion, respuestas):

    mensaje_normalizado = normalizar_texto(mensaje)

    frases = respuestas.get("frases", {})

    for frase, respuesta in frases.items():

        if normalizar_texto(frase) == mensaje_normalizado:
            return respuesta

    intenciones = respuestas.get("intenciones", {})

    if intencion in intenciones:
        return intenciones[intencion][0]

    return "Todavía no sé responder eso."
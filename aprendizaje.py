import json
import os

ARCHIVO_ENTRENAMIENTO = "entrenamiento.json"


def guardar_entrenamiento(entrenamiento):
    with open(ARCHIVO_ENTRENAMIENTO, "w", encoding="utf-8") as archivo:
        json.dump(
            entrenamiento,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def aprender_memoria(mensaje, memoria):

    mensaje_original = mensaje
    mensaje = mensaje.lower()

    if mensaje.startswith("recuerda que "):

        contenido = mensaje_original[13:].strip()

        if " es " in contenido:

            clave, valor = contenido.split(" es ", 1)

            clave = clave.strip()
            valor = valor.strip().rstrip(".")

            clave = clave.replace("mi ", "")
            clave = clave.replace("mis ", "")

            memoria[clave] = valor

            from memoria import guardar_memoria
            guardar_memoria(memoria)

            return "Lo recordaré, jefe. 🧠"

    return None


def aprender_intencion(mensaje, intencion, entrenamiento):

    intencion = intencion.lower().strip()
    mensaje = mensaje.strip()

    if intencion not in entrenamiento:
        entrenamiento[intencion] = []

    ejemplos_existentes = [
        ejemplo.lower()
        for ejemplo in entrenamiento[intencion]
    ]

    if mensaje.lower() not in ejemplos_existentes:

        entrenamiento[intencion].append(mensaje)

        guardar_entrenamiento(entrenamiento)

        return f"Aprendido. Ahora sé que '{mensaje}' significa '{intencion}'. 🧠"

    return "Esa frase ya la conocía. 😎"
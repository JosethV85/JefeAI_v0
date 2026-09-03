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
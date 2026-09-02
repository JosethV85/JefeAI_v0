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


print("================================")
print("          JEFEAI v0.2")
print("================================")

while True:

    mensaje = input("Tú > ")

    if mensaje.lower() == "adios":
        print("JefeAI > Nos vemos, jefe.")
        break

    intencion = analizar_mensaje(mensaje)

    respuesta = responder(intencion)

    print("JefeAI >", respuesta)
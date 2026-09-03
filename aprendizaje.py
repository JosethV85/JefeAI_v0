from memoria import guardar_memoria


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

            guardar_memoria(memoria)

            return "Lo recordaré, jefe. 🧠"

    return None
from memoria import cargar_memoria, guardar_memoria, consultar_memoria
from aprendizaje import aprender_memoria, aprender_intencion, aprender_respuesta
from cerebro import  cargar_entrenamiento, cargar_respuestas, analizar_mensaje, responder, normalizar_texto

memoria = cargar_memoria()
entrenamiento = cargar_entrenamiento()
respuestas = cargar_respuestas()


print("================================")
print("          JEFEAI v0.6")
print("================================")


while True:

    mensaje = input("Tú > ")


    # APRENDIZAJE

    respuesta_memoria = aprender_memoria(mensaje, memoria)

    if respuesta_memoria:

        print("JefeAI >", respuesta_memoria)

        continue


    # CONSULTAR MEMORIA

    respuesta_consulta = consultar_memoria(mensaje, memoria)

    if respuesta_consulta:

        print("JefeAI >", respuesta_consulta)

        continue


    # SALIR

    if mensaje.lower() == "adios":

        guardar_memoria(memoria)

        print("JefeAI > Nos vemos, jefe.")

        break


    # CEREBRO

    intencion = analizar_mensaje(mensaje, entrenamiento)

    if intencion == "desconocido":

        print("JefeAI > No conozco esa frase todavía. 🤔")

        nueva_intencion = input(
            "JefeAI > ¿Qué intención tiene? > "
        ).strip().lower()

        if nueva_intencion:

            respuesta_aprendizaje = aprender_intencion(
                mensaje,
                nueva_intencion,
                entrenamiento
            )

            print("JefeAI >", respuesta_aprendizaje)

        continue


    frases = respuestas.get("frases", {})
    intenciones = respuestas.get("intenciones", {})

    mensaje_normalizado = normalizar_texto(mensaje)

    frases_normalizadas = {
        normalizar_texto(frase): respuesta
        for frase, respuesta in frases.items()
    }

    if mensaje_normalizado not in frases_normalizadas:

        if intencion not in intenciones:

            print("JefeAI > Sé qué significa, pero no sé qué responder. 🤔")

            nueva_respuesta = input(
                "JefeAI > ¿Qué debería responder? > "
            ).strip()

            if nueva_respuesta:

                respuesta_aprendizaje = aprender_respuesta(
                    mensaje,
                    intencion,
                    nueva_respuesta,
                    respuestas
                )

                print("JefeAI >", respuesta_aprendizaje)

            continue


    respuesta = responder(mensaje, intencion, respuestas)

    print("JefeAI >", respuesta)
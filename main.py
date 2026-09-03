from memoria import cargar_memoria, guardar_memoria, consultar_memoria
from aprendizaje import aprender_memoria
from cerebro import analizar_mensaje, responder


memoria = cargar_memoria()


print("================================")
print("          JEFEAI v0.4")
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

    intencion = analizar_mensaje(mensaje)

    respuesta = responder(intencion)

    print("JefeAI >", respuesta)
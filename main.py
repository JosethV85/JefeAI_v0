print("================================")
print("          JEFEAI v0.1")
print("================================")

while True:

    mensaje = input("Tú > ")

    if mensaje.lower() == "hola":
        print("JefeAI > Hola jefe 😎")

    elif mensaje.lower() == "como estas":
        print("JefeAI > Todo bien, jefe.")

    elif mensaje.lower() == "adios":
        print("JefeAI > Nos vemos, jefe.")
        break

    else:
        print("JefeAI > Todavía no sé responder eso.")
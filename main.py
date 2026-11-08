import ollama


class AgenteIA:
    """Agente básico de IA conectado a un modelo local."""

    def __init__(self, modelo="gemma4:e2b"):
        self.modelo = modelo
        self.historial = []

        print(f"🤖 Agente iniciado con el modelo: {self.modelo}")
        print("Escribe 'salir' para terminar.\n")

    def responder(self, mensaje):
        """Envía el mensaje al modelo y devuelve su respuesta."""

        self.historial.append({
            "role": "user",
            "content": mensaje
        })

        respuesta = ollama.chat(
            model=self.modelo,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un asistente de inteligencia artificial "
                        "útil, claro y especializado en programación "
                        "y tecnología. Explica paso a paso."
                    )
                },
                *self.historial
            ]
        )

        texto = respuesta["message"]["content"]

        self.historial.append({
            "role": "assistant",
            "content": texto
        })

        return texto


def main():
    agente = AgenteIA()

    while True:
        mensaje = input("Tú: ").strip()

        if mensaje.lower() == "salir":
            print("Agente: ¡Hasta pronto!")
            break

        if not mensaje:
            continue

        try:
            respuesta = agente.responder(mensaje)
            print(f"\nAgente: {respuesta}\n")

        except Exception as error:
            print(f"\nError al consultar el modelo: {error}")
            print("Comprueba que Ollama esté ejecutándose.\n")


if __name__ == "__main__":
    main()

from strands import Agent
from strands.models.ollama import OllamaModel

PREGUNTA = "Tengo arroz, huevos y verduras. ¿Qué puedo cocinar?"

SYSTEM_PROMPT = """
Sos un ayudante de cocina práctico y cuidadoso.

Tu objetivo es recomendar comidas posibles a partir de ingredientes,
tiempo disponible, preferencias y restricciones alimentarias.

Si la consulta no tiene relación con cocina, recetas, ingredientes
o planificación de comidas, respondé brevemente que solo podés ayudar
con temas de cocina.
"""


def main(
    prompt: str = PREGUNTA,
):
    modelo = OllamaModel(
        host="http://localhost:11434",
        model_id="llama3.1",
    )

    agente = Agent(
        model=modelo,
        system_prompt=SYSTEM_PROMPT,
    )

    print(f"Prompt: {prompt}\n")
    print("Agente: ", end="", flush=True)
    agente(prompt)
    print()


if __name__ == "__main__":
    main()

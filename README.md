# Cooking Agent - Ayudante de cocina con IA local

Repositorio de apoyo para un taller paso a paso sobre construcción de agentes de IA aplicados a recomendaciones de cocina.

El proyecto construye un ayudante de cocina que corre en la computadora usando [Strands Agents SDK](https://github.com/strands-agents/sdk-python) y Ollama. Cada branch representa un paso incremental del tutorial.

---

## Pasos del tutorial

Cada branch es un paso incremental. Empezá por el 1 y seguí en orden.

| # | Branch | Concepto |
|---|--------|----------|
| 1 | `main` | El agente más básico: modelo + prompt |
| 2 | `feature/01b-primer-agente` | Agente interactivo: aceptá prompts del usuario |
| 3 | `feature/02-system-prompt` | Rol y alcance del agente con system prompt |
| 4 | `feature/03-herramientas` | Primera herramienta (`@tool`) para consultar datos |
| 5 | `feature/03b-herramientas-callback` | Visualizar lo que hace el agente con callback |
| 6 | `feature/04-varias-tools` | Múltiples herramientas y decisión del modelo |
| 7 | `feature/05-memoria` | Sesiones para recordar preferencias entre ejecuciones |
| 8 | `feature/06-loop` | Loop interactivo para conversar con el agente |
| 9 | `feature/07-mejoras` | Organización del proyecto Python |
| 10 | `feature/08-modelos` | Cambio a otro modelo o proveedor |

```bash
git switch feature/01b-primer-agente
```

---

## Setup

### Requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) para crear el entorno, instalar dependencias y ejecutar el proyecto
- [Ollama](https://ollama.com/download) para ejecutar el modelo local

### Instalar uv en Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Después cerrá y abrí la terminal, y verificá:

```powershell
uv --version
```

Si aparece un error como `uv: The term 'uv' is not recognized`, copiá el error completo y pegalo en un chatbot para pedir ayuda. Normalmente significa que uv no está instalado o que la terminal todavía no tomó el PATH.

### Instalación

```bash
# Descargar modelo local usado en la presentación
ollama pull llama3.1

# Instalar dependencias con uv
uv sync
```

### Dataset

En los pasos con herramientas, el agente puede consultar una base de recetas.

```bash
mkdir -p data
curl -o data/recetas.json \
  URL_DEL_DATASET/recetas.json
```

### Ejecutar

```bash
uv run main.py
```

---

## ¿Qué aprendés?

```text
[Paso 1-2] Modelo + Prompt -> Agente con rol y alcance
[Paso 3-4] Agente + @tool -> Consulta datos reales y decide qué herramienta usar
[Paso 5-6] Session Manager + Loop -> Memoria + interfaz interactiva
[Paso 7-8] Organización + Modelos -> Código más claro y cambio de proveedor
```

---

## Recursos

- [Strands Agents SDK](https://github.com/strands-agents/sdk-python)
  - [Strands Agents Docs](https://strandsagents.com/)
- [Ollama](https://ollama.com/download)
- [ADK](https://adk.dev/get-started/python/)

---

## Agradecimientos

Material adaptado para una práctica propia sobre agentes de IA, modelos locales y herramientas.

---

## License

MIT

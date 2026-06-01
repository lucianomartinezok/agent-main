# Paso a paso para correr el ayudante de cocina

Este proyecto es un ayudante de cocina con IA local. Usa Python para ejecutar el agente, Strands Agents para organizar la lógica del agente y Ollama para correr el modelo en la computadora.

1. Abrir una terminal.

En Windows podés usar PowerShell o CMD. En macOS podés usar Terminal.

2. Ir a la carpeta del proyecto.

Ruta del proyecto:
C:\00\agent-main

Comando:
cd C:\00\agent-main

3. Verificar Python.

En Windows probá:
py --version

Si ese comando no funciona, probá:
python --version

En macOS probá:
python3 --version

El proyecto pide Python 3.13 o superior. Si la terminal no reconoce Python, cerrá y abrí la terminal después de instalarlo, o revisá que Python esté agregado al PATH.

4. Verificar uv.

Comando:
uv --version

uv se usa para crear el entorno de Python del proyecto, instalar las dependencias y ejecutar main.py sin activar el entorno manualmente.

Si uv no está instalado en Windows, podés instalarlo con:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Después cerrá y abrí una terminal nueva, y repetí:
uv --version

Si la terminal muestra un error como:
uv: The term 'uv' is not recognized as a name of a cmdlet, function, script file, or executable program.

Eso significa que uv no está instalado o que Windows todavía no lo encuentra en el PATH. Copiá el error completo y pegalo en un chatbot para pedir ayuda con el diagnóstico.

5. Verificar Ollama.

Comando:
ollama --version

Ollama tiene que estar instalado y disponible desde la terminal. Si la terminal no reconoce el comando, abrí la aplicación de Ollama, reinstalá si hace falta o abrí una terminal nueva para que tome el PATH.

6. Descargar el modelo.

Comando:
ollama pull llama3.1

La presentación queda preparada para llama3.1 porque es más liviano para equipos personales. Modelos más grandes pueden consumir mucha memoria y colgar la computadora.

7. Confirmar que el modelo quedó disponible.

Comando:
ollama list

En la lista debería aparecer llama3.1. Si no aparece, repetí la descarga o revisá que Ollama esté corriendo.

8. Instalar dependencias del proyecto.

Comando:
uv sync

Esto lee pyproject.toml y prepara las librerías necesarias, incluyendo Strands Agents con soporte para Ollama.

Si falla, copiá el mensaje completo de error. Es importante incluir el comando que ejecutaste y toda la salida de la terminal.

9. Ejecutar el agente.

Comando:
uv run main.py

El script envía esta consulta inicial:
Tengo arroz, huevos y verduras. ¿Qué puedo cocinar?

La respuesta esperada es una recomendación de cocina generada por el modelo local.

10. Qué hace la versión actual.

La rama principal muestra el agente base: conecta Python, Strands Agents, Ollama y el modelo llama3.1.

Todavía no consulta data/recetas.json en main.py. Ese dataset aparece en pasos posteriores de la presentación, cuando se agregan herramientas con @tool.

11. Consistencia con la presentación.

La presentación habla de un agente de recomendaciones de cocina y el código ahora usa ese mismo dominio.

main.py usa llama3.1, igual que la diapositiva de selección de modelo en Ollama.

pyproject.toml identifica el proyecto como cooking-agent y pide Python 3.13 o superior.

README.md explica el setup con Ollama, llama3.1, uv y data/recetas.json para los pasos con herramientas.

Las diapositivas muestran data/recetas.json para la parte de herramientas. Eso coincide con el README, pero no es necesario para ejecutar el main.py básico.

12. Estado verificado desde esta terminal.

En la terminal usada para esta revisión, los comandos python, uv y ollama no están disponibles en el PATH. Por eso no se pudo ejecutar uv run main.py desde acá.

El código y la documentación quedaron alineados. Para correrlo en tu máquina, primero asegurate de que Python, uv y Ollama respondan desde la terminal donde vas a ejecutar el proyecto.

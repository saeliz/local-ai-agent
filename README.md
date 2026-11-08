# Local AI Agent

Agente de inteligencia artificial local desarrollado
con Python y Ollama.

## Tecnologías

- Python
- Ollama
- Gemma 4

## Características

- Inteligencia artificial local.
- Historial de conversación.
- Procesamiento de mensajes.
- Respuestas contextualizadas.

## Instalación

```bash
git clone https://github.com/TU-USUARIO/local-ai-agent.git
cd local-ai-agent

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
ollama pull gemma4:e2b

python main.py
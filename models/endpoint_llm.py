import json
import requests
from config import LLM_ENDPOINT, MODEL_NAME

class FunctionCallObj:
    """Standardized representation of a tool call matching executor expectation."""
    def __init__(self, name: str, args: dict):
        self.name = name
        self.args = args

class ModelResponse:
    """Normalized response object for AgentLoop."""
    def __init__(self, text: str, function_calls=None):
        self.text = text
        self.function_calls = function_calls or []

class EndpointModel:
    """
    Client wrapper that talks to your custom self-hosted endpoint
    (OpenAI-compatible / vLLM / Ollama / FastAPI backend).
    Users do NOT need any API keys to use this.
    """
    def __init__(self, endpoint=LLM_ENDPOINT, model_name=MODEL_NAME):
        self.endpoint = endpoint
        self.model_name = model_name
        self.messages = []
        self.tools = []

    def start_chat(self, tools=None, system_instruction=None):
        self.messages = []
        if system_instruction:
            self.messages.append({
                "role": "system",
                "content": str(system_instruction)
            })

    def generate(self, content):
        self.messages.append({
            "role": "user",
            "content": str(content)
        })

        payload = {
            "model": self.model_name,
            "messages": self.messages,
            "temperature": 0.2
        }

        try:
            resp = requests.post(
                self.endpoint,
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=60
            )
            resp.raise_for_status()
            data = resp.json()

            # Handles standard OpenAI / vLLM format
            choice = data["choices"][0]["message"]
            reply_text = choice.get("content", "") or ""

            # Check for tool / function calls in standard format
            function_calls = []
            if "tool_calls" in choice and choice["tool_calls"]:
                for tc in choice["tool_calls"]:
                    fn_name = tc["function"]["name"]
                    fn_args = tc["function"]["arguments"]
                    if isinstance(fn_args, str):
                        fn_args = json.loads(fn_args)
                    function_calls.append(FunctionCallObj(fn_name, fn_args))
            
            # Record assistant reply in conversation memory
            self.messages.append({
                "role": "assistant",
                "content": reply_text
            })

            return ModelResponse(text=reply_text, function_calls=function_calls)

        except Exception as e:
            return ModelResponse(
                text=f"Error connecting to custom endpoint ({self.endpoint}): {str(e)}",
                function_calls=[]
            )

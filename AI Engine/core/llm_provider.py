import os
import json
import requests

class LLMProvider:
    """
    Abstracts LLM interaction. Designed to be interchangeable.
    Supports OpenAI, Gemini (via HTTP) or any OpenAI-compatible API (like Groq/OpenRouter).
    """

    def __init__(self):
        self.api_key = os.getenv("OPTIMAX_API_KEY")
        self.provider = os.getenv("OPTIMAX_PROVIDER", "openai").lower() # openai, gemini, groq
        self.model = os.getenv("OPTIMAX_MODEL", "gpt-3.5-turbo")

    def call(self, system_prompt: str, user_prompt: str) -> dict:
        if not self.api_key:
            raise ValueError("OPTIMAX_API_KEY environment variable is not set.")

        if self.provider == "openai" or self.provider == "groq":
            return self._call_openai_compatible(system_prompt, user_prompt)
        elif self.provider == "gemini":
            return self._call_gemini(system_prompt, user_prompt)
        else:
            raise ValueError(f"Provider {self.provider} not supported.")

    def _call_openai_compatible(self, system_prompt: str, user_prompt: str) -> dict:
        url = "https://api.openai.com/v1/chat/completions"
        if self.provider == "groq":
            url = "https://api.groq.com/openai/v1/chat/completions"
            self.model = os.getenv("OPTIMAX_MODEL", "llama3-8b-8192")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "response_format": {"type": "json_object"}
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        content = response.json()["choices"][0]["message"]["content"]
        return json.loads(content)

    def _call_gemini(self, system_prompt: str, user_prompt: str) -> dict:
        # Simplified Gemini API call
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        
        headers = {"Content-Type": "application/json"}
        full_prompt = f"{system_prompt}\n\nContext:\n{user_prompt}"
        
        payload = {
            "contents": [{
                "parts": [{"text": full_prompt}]
            }],
            "generationConfig": {
                "response_mime_type": "application/json"
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        content = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return json.loads(content)

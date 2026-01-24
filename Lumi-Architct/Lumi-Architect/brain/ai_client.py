"""
Lumi: Architect - AI Client
===========================
Handles communication with the OpenAI API to generate Architecture Manifests.
"""

import os
import sys
from typing import Optional
from openai import OpenAI
from brain.prompt_engine import PromptEngine, PromptEngineResult

class AIClient:
    """
    Client for interacting with the AI model.
    """
    
    def __init__(self, model: str = "gpt-4o"):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model
        self.engine = PromptEngine()
        
        if not self.api_key or self.api_key == "your_api_key_here":
            self._handle_missing_key()
            
        try:
            self.client = OpenAI(api_key=self.api_key)
        except Exception as e:
            print(f"Error: Fallo al inicializar el cliente de OpenAI: {e}")
            sys.exit(1)

    def _handle_missing_key(self):
        """Prints a professional error message and exits safely."""
        print("\n" + "="*80)
        print(" ERROR: Configuración de API no encontrada.")
        print("="*80)
        print("\n Por favor, asegúrese de que el archivo .env contenga una OPENAI_API_KEY válida.")
        print(" Puede copiar el archivo .env.example como .env y completar su clave real.")
        print("\n Ruta esperada: Lumi-Architct/.env")
        print("="*80 + "\n")
        sys.exit(1)

    def generate_manifest(self, user_request: str, system_context: Optional[dict] = None) -> PromptEngineResult:
        """
        Sends a request to the AI model and returns the parsed manifest.
        """
        prompts = self.engine.prepare_request(user_request, system_context)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompts["system"]},
                    {"role": "user", "content": prompts["user"]}
                ],
                temperature=0.2, # Lower temperature for more structured output
            )
            
            raw_content = response.choices[0].message.content
            return self.engine.parse_response(raw_content)
            
        except Exception as e:
            return PromptEngineResult(
                success=False,
                error=f"Error en la llamada a la API de OpenAI: {str(e)}"
            )

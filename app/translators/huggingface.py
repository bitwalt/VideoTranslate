import requests
from typing import Optional
from .base_translator import BaseTranslator

MODEL_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-it"
API_TOKEN = ""

class HuggingFaceTranslator(BaseTranslator): 

    def __init__(self, api_token: str, model_url: str = MODEL_URL):
        self.api_url = model_url
        self.api_token = api_token
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
    
    def translate_text(self, text: str, target_language: str, source_language: Optional[str] = None) -> str:
        """Implementation of abstract method from BaseTranslator."""
        payload = {"inputs": text}
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        result = response.json()
        
        if isinstance(result, list) and len(result) > 0:
            return result[0].get('translation_text', '')
        return str(result)  # Fallback case
        
    def test_query(self):
        text = """
            Eight thousand years ago, mesopotamia
            tribes were the first to utilize a
            bartering system to get the food 
            weapons and spices they needed.
            These ancient people realized they could use
            their time to create value for others. 
            In return they exchange
            this value for other goods and services.
            This idea has merged into the
            advancement of the human species,
            today that same process is still intact.
            It's called the economy.
            Or now, it's called bitcoin.
        """
        return  self.query({"inputs": text})
        
        
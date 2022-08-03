import requests


class HuggingTranslator: 

    def __init__(self, cfg):
        self.API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-it"
        self.API_TOKEN = ""
    
    def query(self, payload):
        headers = {"Authorization": f"Bearer {self.API_TOKEN}"}
        response = requests.post(self.API_URL, headers=headers, json=payload)
        return response.json()
	
    def translate(self, input_text):
            output_text = self.query(input_text)
            return output_text
        
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
        
        
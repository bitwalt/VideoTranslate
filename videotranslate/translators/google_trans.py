import googletrans
import requests

class GoogleTranslator: 


    def __init__(self, cfg): 
        
        self.model  = googletrans.Translator(service_urls=['translate.google.com'])

    def get_languages(self):
        return googletrans.LANGUAGES
    
    def translate(self, scr:str, dst:str , input_text:str):
            
        sour = self.model.detect(input_text).lang
        answer = self.model.translate(input_text, src=f'{sour}', dest=f'{dst}').text
        return answer
    
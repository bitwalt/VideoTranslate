import deepl
from typing import Optional, Dict
from .base_translator import BaseTranslator

class DeepLTranslator(BaseTranslator):
    """DeepL API translator implementation."""
    
    def __init__(self, api_key: str, is_free_api: bool = True):
        """
        Initialize DeepL translator.
        
        Args:
            api_key: DeepL API authentication key
            is_free_api: Whether using free or pro API (defaults to free)
        """
        self.translator = deepl.Translator(api_key, server_url="api-free.deepl.com" if is_free_api else "api.deepl.com")
    
    def translate_text(self, text: str, target_language: str, source_language: Optional[str] = None) -> str:
        """
        Translate text using DeepL API.
        
        Args:
            text: Text to translate
            target_language: Target language code (e.g., 'EN-US', 'DE', 'FR')
            source_language: Source language code (optional)
            
        Returns:
            Translated text
        """
        try:
            result = self.translator.translate_text(
                text,
                target_lang=target_language.upper(),
                source_lang=source_language.upper() if source_language else None
            )
            return str(result)
        except deepl.exceptions.DeepLException as e:
            raise Exception(f"DeepL translation failed: {str(e)}")
    
    def get_supported_languages(self) -> Dict[str, str]:
        """Get dictionary of supported target languages."""
        try:
            languages = self.translator.get_target_languages()
            return {lang.code: lang.name for lang in languages}
        except deepl.exceptions.DeepLException as e:
            raise Exception(f"Failed to get supported languages: {str(e)}")
    
    def translate_batch(self, texts: list[str], target_language: str, source_language: Optional[str] = None) -> list[str]:
        """
        Translate multiple texts in one API call for better performance.
        
        Args:
            texts: List of texts to translate
            target_language: Target language code
            source_language: Source language code (optional)
            
        Returns:
            List of translated texts
        """
        try:
            results = self.translator.translate_text(
                texts,
                target_lang=target_language.upper(),
                source_lang=source_language.upper() if source_language else None
            )
            return [str(result) for result in results]
        except deepl.exceptions.DeepLException as e:
            raise Exception(f"DeepL batch translation failed: {str(e)}") 
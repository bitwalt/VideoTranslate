from abc import ABC, abstractmethod
from typing import Optional, Union, Dict
from pathlib import Path

class BaseTranslator(ABC):
    """Abstract base class for all translator implementations."""
    
    @abstractmethod
    def translate_text(self, text: str, target_language: str, source_language: Optional[str] = None) -> str:
        """Translate text from source language to target language."""
        pass
    
    def translate_batch(self, texts: list[str], target_language: str, source_language: Optional[str] = None) -> list[str]:
        """Default batch translation implementation."""
        return [self.translate_text(text, target_language, source_language) for text in texts]
    
    def get_supported_languages(self) -> Dict[str, str]:
        """Get dictionary of supported languages. Optional to implement."""
        raise NotImplementedError("Supported languages list not available for this translator") 
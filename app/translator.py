from translators.base_translator import BaseTranslator
from translators.openai import OpenAITranslator
from translators.deepl_trans import DeepLTranslator
from translators.huggingface import HuggingFaceTranslator
from config import TranslatorModel

class TranslatorFactory:
    @staticmethod
    def create_translator(config) -> BaseTranslator:
        model = config.get('translator', {}).get('model', TranslatorModel.OPENAI)
        
        if model == TranslatorModel.OPENAI:
            return OpenAITranslator(
                api_key=config['translator']['api_key'],
                model=config['translator']['model_name'],
                audio_model=config['translator']['audio_model']
            )
        elif model == TranslatorModel.DEEPL:
            return DeepLTranslator(api_key=config['translator']['api_key'])
        elif model == TranslatorModel.HUGGINGFACE:
            return HuggingFaceTranslator(api_token=config['translator']['api_key'])
        else:
            raise ValueError(f"Unsupported translator model: {model}")
from enum import Enum, auto
from translators.google_trans import GoogleTranslator
from translators.huggingface import HuggingTranslator


class TranslatorModel(Enum):
    GOOGLETRANS =  auto()
    HUGGINGFACE = auto()
    DEEPL = auto()


class Translator:
    
    def __init__(self, cfg):
    
        self.mode = cfg['mode']
        if self.mode == TranslatorModel.HUGGINGFACE:
            self.model = HuggingTranslator(cfg)
        elif self.mode == TranslatorModel.GOOGLETRANS:
            self.model = GoogleTranslator(cfg)

    def get_model(self, mode):
        pass
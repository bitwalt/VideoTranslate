from enum import Enum, auto
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_MODEL_NAME = "gpt-4o-mini"
WHISPER_MODEL_NAME = "whisper-1"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

class TranslatorModel(Enum):
    OPENAI = auto()
    DEEPL = auto()
    GOOGLETRANS = auto()
    HUGGINGFACE = auto()

DEFAULT_CONFIG = {
    "translator": {
        "model": TranslatorModel.OPENAI,
        "api_key": OPENAI_API_KEY,  # Should be set via environment variable
        "model_name": OPENAI_MODEL_NAME,
        "audio_model": WHISPER_MODEL_NAME
    },
    "language": {
        "source": "en",
        "target": "it"
    },
    "output": {
        "format": "txt",
        "folder": "./output/"
    }
}



TRANSLATOR_MODELS = ['GoogleTranslator', 'HuggingFace', 'DeepL', 'G-Cloud']  
SP2_MODELS = ['Google gTTS (free)', 'HuggingFace', 'G-Cloud']  

cfg = {
    "videos": {
        "PScIpF9Wjpc": "Il Bitcoin Standard"   
    },
    "process": ["Download", "Transcript", "AI-Translate"],
    "formatter": "txt",
    "output_folder": "./output/",
    "language_from": "en",
    "language_to": "it"
}


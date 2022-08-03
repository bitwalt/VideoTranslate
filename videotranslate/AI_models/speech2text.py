from gtts import gTTS 


class Speech2Text:
    
    def __init__(self, source):
        self.source = source 

    def get_audio_from_text(self, text):
        ta_tts = gTTS(text,lang=f'{self.source}')
        ta_tts.save(f'{self.source}_transcrition.mp3')
     

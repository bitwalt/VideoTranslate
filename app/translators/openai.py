from pathlib import Path
from typing import Optional, Union
from config import OPENAI_MODEL_NAME, WHISPER_MODEL_NAME
from openai import OpenAI

# Translation prompt templates
DEFAULT_TRANSLATION_PROMPT = "Translate the following text to {target_language}:\n{text}"
DEFAULT_TRANSLATION_PROMPT_WITH_SOURCE = "Translate the following {source_language} text to {target_language}:\n{text}"
DEFAULT_SYSTEM_PROMPT = "You are a professional translator."

class OpenAITranslator:
    def __init__(self, api_key: str, 
                 model: str = OPENAI_MODEL_NAME,
                 audio_model: str = WHISPER_MODEL_NAME,
                 translation_prompt: str = DEFAULT_TRANSLATION_PROMPT,
                 translation_prompt_with_source: str = DEFAULT_TRANSLATION_PROMPT_WITH_SOURCE,
                 system_prompt: str = DEFAULT_SYSTEM_PROMPT):
        """Initialize OpenAI translator with API key and custom prompts."""
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.audio_model = audio_model
        self.translation_prompt = translation_prompt
        self.translation_prompt_with_source = translation_prompt_with_source
        self.system_prompt = system_prompt

    def translate_text(self, text: str, target_language: str, source_language: Optional[str] = None) -> str:
        """Translate text using OpenAI's GPT model."""
        prompt = self.translation_prompt.format(target_language=target_language, text=text)
        if source_language:
            prompt = self.translation_prompt_with_source.format(
                source_language=source_language,
                target_language=target_language,
                text=text
            )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")

    def transcribe_audio(self, audio_file: Union[str, Path], language: Optional[str] = None) -> str:
        """Transcribe audio file using OpenAI's Whisper model."""
        try:
            audio_path = Path(audio_file)
            if not audio_path.exists():
                raise FileNotFoundError(f"Audio file not found: {audio_file}")

            with open(audio_path, "rb") as audio:
                response = self.client.audio.transcriptions.create(
                    model=self.audio_model,
                    file=audio,
                    language=language
                )
            return response.text
        except Exception as e:
            raise Exception(f"Transcription failed: {str(e)}")

    def translate_video(self, video_path: Union[str, Path], target_language: str) -> dict:
        """
        Transcribe and translate a video file.
        
        Args:
            video_path: Path to video file
            target_language: Language to translate to
            
        Returns:
            Dictionary containing original transcription and translation
        """
        try:
            # First, transcribe the video
            transcription = self.transcribe_audio(video_path)
            
            # Then translate the transcription
            translation = self.translate_text(transcription, target_language)
            
            return {
                "original_text": transcription,
                "translated_text": translation
            }
        except Exception as e:
            raise Exception(f"Video translation failed: {str(e)}")

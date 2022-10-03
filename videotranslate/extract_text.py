import os, json
import logging
from utils import set_logger
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter, TextFormatter


class YoutubeTextExtractor:
    
    def __init__(self, f_type:str):
        self.f_type = f_type
        if f_type=="Text":
            self.formatter = TextFormatter()
        else:
            self.formatter = JSONFormatter()
        
                 
    def get_transcript_from_id(self, video_id: str):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)    
            text_formatted = self.formatter.format_transcript(transcript, indent=4)
            return text_formatted
        except Exception as e:
            logging.error(e)
            logging.error(f"Failed to get text from {video_id}")
            return None
        
        
    def save_text(self, transcript: str, file_path: str):
        try:
            # file_name = os.path.join(self.output_dir, video_name + f".{self.f_type}")
            if not os.path.exists(file_path) and transcript:         
                with open(file_path, "w") as f:
                    f.write(transcript)
                    logging.info(f"Saved {file_path}")
            else:
                logging.warning(f"Skipped saving video original text: {file_path}")
        except Exception as e:
            logging.error(f"Failed to save text to {file_path}")
        
    @staticmethod 
    def translate_from_id(video_id: str, lang: str="en", target_lang: str="it"):
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript([lang])
            if transcript:
                translated_transcript = transcript.translate(target_lang)
                translated_text = translated_transcript.fetch()
                return json.dumps(translated_text, indent=4)
            else:
                return None 
        except Exception as e:
            logging.error(e)
            logging.error(f"Failed to translate text")
            return None
      
    def extract_from_ids(self, videos: dict):
        for video_id, video_name in videos.items():
            text = self.get_text(video_id)
            self.save_text(text, video_name)
            
    def translate_from_ids(self, videos: dict, language_from: str, language_to: str):
        for video_id, video_name in videos.items():
            translated_text = self.translate_from_id(video_id, language_from, language_to)
            self.save_text(translated_text, "ITA_"+video_name)
                 

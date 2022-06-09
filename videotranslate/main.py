from extract_text import TextExtractor
from video_download import VideoDownloader
from utils import load_config

if __name__ == "__main__":
    cfg = load_config("config.json")  
    videos = cfg['videos']
    language_from = cfg['language_from']
    language_to = cfg['language_to']
    
    text_extractor = TextExtractor(cfg['output_folder'], f_type=cfg['formatter'])
    video_downlaoder = VideoDownloader(cfg['output_folder'])
    
    # Save original captions
    text_extractor.extract_from_ids(videos)
    # Translate original captions in italian
    text_extractor.translate_from_ids(videos, language_from, language_to)
    
    # Downlaod videos
    for video_id, video_name in videos.items():
        video_downlaoder.downlaod_video(video_id, video_name)
    
import os    
import logging
from pytube import YouTube

class VideoDownloader:
    def __init__(self, output_dir: str):
        self.saving_dir = os.path.join(output_dir, "videos")
        if not os.path.exists(self.saving_dir):
            os.makedirs(self.saving_dir)        
    
    def downlaod_video(self, video_id: str, video_name: str):
        try:
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if os.path.exists(os.path.join(self.saving_dir, video_name + ".mp4")):
                logging.warning(f"Downloading video {video_name} skipped")
            else:
                video.download(self.saving_dir, filename=video_name+".mp4")
                logging.info(f"Downloaded video: {video_name}")
        except Exception as e:
            logging.error(e)
            logging.error(f"Failed to download video: {video_name}")
            
    
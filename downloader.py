"""
Downloader module
"""

import yt_dlp
from config import AUDIO_QUALITY, DEFAULT_DOWNLOAD_PATH, FFMPEG_PATH, DEFAULT_AUDIO_FORMAT, 

class Downloader:
    def __init__(self, download_path=None):
        # downloader with custom download path
        self.download_path == download_path or DEFAULT_DOWNLOAD_PATH
        self.progress_callback = None

    def set_progress_callback(self, callback):
        # call back function for progress updates
        self.progress_callback = callback 
    
    def _progress_hook(self, d):
    
        if self.progress_callback:
            if d['status'] == 'downloading':
                progress_info = {
                    # Extract progress info
                    'status': 'downloading',
                    'percent': d.get('_percent_str', '0%'),
                    'speed': d.get('_speed_str', 'N/A'),
                    'eta': d.get('_eta_str', 'N/A')
                }
                self.progress_callback(progress_info)

            elif d['status'] == 'finish':
                self.progress_callback({'status': 'finished', 'message': 'Download complete, converting...'})

    def download_audio(self, url, audio_format=None):
        """
        download and convert audio
        
        Args:
            url: URL of the video to download
            audio format: Audio format (default from config)
        
        Returns:
        """
        # yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_format,
                'preferredquality': AUDIO_QUALITY,
            }]
        }

        #Add ffmpeg location if specified
        if FFMPEG_PATH:
            ydl_opts['ffmpeg_loaction'] = FFMPEG_PATH

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
"""
Downloader module
"""

import yt-dlp
from config import DEFAULT_DOWNLOAD_PATH, FFMPEG_PATH, DEFAULT_AUDIO_FORMAT, 

class Downloader:
    def __init__(self, download_path=None):
        # downloader with custom download path
        self.download_path == download_path or DEFAULT_DOWNLOAD_PATH
        self.progress_callback = None

    def set_progress_callback(self, callback):
        # call back function for progress updates
        self.progress_callback = callback
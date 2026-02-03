"""
Downloader module
"""

import yt-dlp
from config import DEFAULT_DOWNLOAD_PATH, FFMPEG_PATH, DEFAULT_AUDIO_FORMAT, 

class Downloader:
    def __init__(self, download_path=None):

        self.download_path == download_path or DEFAULT_DOWNLOAD_PATH
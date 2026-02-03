"""
Configuration file for yt-dlp GUI
Stores default settings and paths
"""
import os

# Default download directory (change path as desired)
DEFAULT_DOWNLOAD_PATH = os.path.join(os.path.expanduse("~"), "Downloads", "yt-dlp")

# path to ffmpeg when in specific location; write None if using system PATH
FFMPEG_PATH = r"C:\ytdl\ffmpeg.exe" # location of the ffmpeg script

# default audio format
DEFAULT_AUDIO_FORMAT = "mp3"

# audio quality 0-9 (best to worst)
AUDIO_QUALITY = "0"

#create download path if it does not exist
if not os.path.exists(DEFAULT_DOWNLOAD_PATH):
    os.makedirs(DEFAULT_DOWNLOAD_PATH)
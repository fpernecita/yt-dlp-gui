import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from downloader import Downloader
from config import DEFAULT_DOWNLOAD_PATH

class YtDlpGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("yt-dlp Audio Downloader")
        self.root.geometry("600x400")
        # initialise downloader
        self.downloader = Downloader()
        self.downloader.set_progress_callback(self.update_progress)
        # call widget creation
        self.create_widgets()

    def create_widgets():
        # create all the widgets
        
        
    def browse_folder():
    
    def update_progress():

    def start_download(self):


def main():
    
if __name__ == "__main__":
    main()